import * as vscode from 'vscode';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    const stubPath = path.join(context.extensionPath, 'micropython_lib');
    const pythonConfig = vscode.workspace.getConfiguration('python');

    const extraPaths = pythonConfig.get<string[]>('analysis.extraPaths') || [];
    if (!extraPaths.includes(stubPath)) {
        extraPaths.push(stubPath);
        pythonConfig.update('analysis.extraPaths', extraPaths, vscode.ConfigurationTarget.Workspace);
    }

    vscode.window.showInformationMessage('MicroPython IntelliSense (custom) activated!');
}

export function deactivate() {}