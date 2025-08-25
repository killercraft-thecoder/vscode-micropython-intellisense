import * as vscode from "vscode";
import * as path from "path";
import * as fs from "fs";

export function activate(context: vscode.ExtensionContext) {
  const stubPath = path.join(context.extensionPath, "micropython_lib");
  const pythonConfig = vscode.workspace.getConfiguration("python");

  const extraPaths = pythonConfig.get<string[]>("analysis.extraPaths") || [];
  if (!extraPaths.includes(stubPath)) {
    extraPaths.push(stubPath);
    pythonConfig.update(
      "analysis.extraPaths",
      extraPaths,
      vscode.ConfigurationTarget.Workspace
    );
  }

  const diagnostics =
    vscode.languages.createDiagnosticCollection("micropython");
  context.subscriptions.push(diagnostics);

  const supportedExceptions = new Set([
    "Exception",
    "ValueError",
    "TypeError",
    "OSError",
    "RuntimeError",
    "MemoryError",
    "BaseException"
  ]);

  function getAllowedModules(): Set<string> {
    const allowed = new Set<string>();

    // 1. Non-recursive scan of micropython_lib
    if (fs.existsSync(stubPath)) {
      for (const file of fs.readdirSync(stubPath)) {
        if (file.endsWith(".py")) {
          allowed.add(path.basename(file, ".py"));
        }
      }
    }

    // 2. Recursive scan of workspace folders
    const folders = vscode.workspace.workspaceFolders || [];
    for (const folder of folders) {
      walkFolder(folder.uri.fsPath, allowed);
    }

    return allowed;
  }

  function walkFolder(dir: string, allowed: Set<string>) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);

      if (entry.isDirectory()) {
        walkFolder(fullPath, allowed);
      } else if (entry.isFile()) {
        if (entry.name.endsWith(".py") || entry.name.endsWith(".mpy")) {
          allowed.add(path.basename(entry.name, path.extname(entry.name)));
        }
      }
    }
  }

  function refreshDiagnostics(doc: vscode.TextDocument) {
    if (!doc.fileName.endsWith(".mpy")) {
      return;
    }

    const diags: vscode.Diagnostic[] = [];
    const lines = doc.getText().split(/\r?\n/);
    const allowedModules = getAllowedModules();

    lines.forEach((line, i) => {
      // Unsupported param syntax
      if (/def\s+\w+\s*\([^)]*[/\*][^)]*\)/.test(line)) {
        diags.push(
          new vscode.Diagnostic(
            new vscode.Range(i, 0, i, line.length),
            "This parameter syntax may not be supported in TI‑84 MicroPython.",
            vscode.DiagnosticSeverity.Warning
          )
        );
      }

      // Missing exception classes
      const excMatch = line.match(/\b(?:raise|except)\s+(\w+)/);
      if (excMatch && !supportedExceptions.has(excMatch[1])) {
        diags.push(
          new vscode.Diagnostic(
            new vscode.Range(i, 0, i, line.length),
            `Exception class '${excMatch[1]}' is not available in TI‑84 MicroPython.`,
            vscode.DiagnosticSeverity.Warning
          )
        );
      }

      // Import checks
      const importMatch = line.match(/^\s*(?:from|import)\s+([a-zA-Z0-9_\.]+)/);
      if (importMatch) {
        const rootModule = importMatch[1].split(".")[0];
        if (!allowedModules.has(rootModule)) {
          diags.push(
            new vscode.Diagnostic(
              new vscode.Range(i, 0, i, line.length),
              `Module '${rootModule}' is not built-in to micropython or exist in the workspace`,
              vscode.DiagnosticSeverity.Warning
            )
          );
        }
      }
    });

    diagnostics.set(doc.uri, diags);
  }

  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument(refreshDiagnostics),
    vscode.workspace.onDidChangeTextDocument((e) =>
      refreshDiagnostics(e.document)
    ),
    vscode.workspace.onDidCloseTextDocument((doc) =>
      diagnostics.delete(doc.uri)
    )
  );

  if (vscode.window.activeTextEditor) {
    refreshDiagnostics(vscode.window.activeTextEditor.document);
  }

  vscode.window.showInformationMessage(
    "MicroPython IntelliSense + syntax/import checks activated for .mpy files!"
  );
}

export function deactivate() {}
