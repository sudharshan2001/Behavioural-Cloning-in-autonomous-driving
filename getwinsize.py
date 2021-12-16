import ctypes
from ctypes.wintypes import RECT
from ctypes import wintypes

def GetWindowRectFromName(name):
    hwnd = ctypes.windll.user32.FindWindowW(0, name)
    user32_dll = ctypes.WinDLL("user32")
    get_windows_rect_func = user32_dll.GetWindowRect
    get_windows_rect_func.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
    get_windows_rect_func.restype = wintypes.BOOL
    rect = wintypes.RECT()
    result = get_windows_rect_func(hwnd, ctypes.byref(rect))

    return (rect.left, rect.top, rect.right, rect.bottom)

