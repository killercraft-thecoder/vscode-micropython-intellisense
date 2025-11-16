"""
MicroPython stm module stub.
Provides symbolic constants for STM32F405 registers and direct memory access.
On TI‑84: not available — this is for IntelliSense and optional emulation.
"""

# -------------------------
# Peripheral base addresses
# -------------------------
GPIOA = 0x40020000
GPIOB = 0x40020400
GPIOC = 0x40020800
GPIOD = 0x40020C00
GPIOE = 0x40021000
GPIOF = 0x40021400
GPIOG = 0x40021800
GPIOH = 0x40021C00
GPIOI = 0x40022000

RCC    = 0x40023800
FLASH  = 0x40023C00
PWR    = 0x40007000
SYSCFG = 0x40013800
EXTI   = 0x40013C00
USART1 = 0x40011000
USART2 = 0x40004400
USART3 = 0x40004800
UART4  = 0x40004C00
UART5  = 0x40005000
USART6 = 0x40011400
SPI1   = 0x40013000
SPI2   = 0x40003800
SPI3   = 0x40003C00
I2C1   = 0x40005400
I2C2   = 0x40005800
I2C3   = 0x40005C00
TIM1   = 0x40010000
TIM2   = 0x40000000
TIM3   = 0x40000400
TIM4   = 0x40000800
TIM5   = 0x40000C00
TIM6   = 0x40001000
TIM7   = 0x40001400
TIM8   = 0x40010400

# -------------------------
# Common register offsets
# -------------------------
MODER   = 0x00
OTYPER  = 0x04
OSPEEDR = 0x08
PUPDR   = 0x0C
IDR     = 0x10
ODR     = 0x14
BSRR    = 0x18
LCKR    = 0x1C
AFRL    = 0x20
AFRH    = 0x24

CR      = 0x00
PLL_CFGR= 0x04
CFGR    = 0x08
CIR     = 0x0C
AHB1ENR = 0x30
AHB2ENR = 0x34
APB1ENR = 0x40
APB2ENR = 0x44

SR      = 0x00
DR      = 0x04
BRR     = 0x08
CR1     = 0x0C
CR2     = 0x10
CR3     = 0x14
GTPR    = 0x18

# -------------------------
# Fake memory maps for emulation
# -------------------------
_mem32 = {}
_mem16 = {}
_mem8  = {}

class mem32(dict):
    """Dictionary-like access to 32-bit memory-mapped registers."""
    def __getitem__(self, addr):
        return _mem32.get(addr, 0)
    def __setitem__(self, addr, value):
        _mem32[addr] = value & 0xFFFFFFFF

class mem16(dict):
    """Dictionary-like access to 16-bit memory-mapped registers."""
    def __getitem__(self, addr):
        return _mem16.get(addr, 0)
    def __setitem__(self, addr, value):
        _mem16[addr] = value & 0xFFFF

class mem8(dict):
    """Dictionary-like access to 8-bit memory-mapped registers."""
    def __getitem__(self, addr):
        return _mem8.get(addr, 0)
    def __setitem__(self, addr, value):
        _mem8[addr] = value & 0xFF

# Instantiate the memory access objects
mem32 = mem32() # type:ignore
mem16 = mem16() # type:ignore
mem8  = mem8() # type:ignore