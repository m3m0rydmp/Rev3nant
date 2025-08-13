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

# Obfuscated variable names and functions
class XvKjP9mNqR:
    def __init__(self):
        self.__wMnPqRtY = tk.Tk()
        self.__aLkJhGfD = "Security Assessment"
        self.__zXcVbNmQ = "700x500"
        self.__qWeRtYuI = False
        self.__pOiUyTrE = '#0a0a0a'
        
        # Obfuscated encryption key (base64 encoded)
        self.__kEyEnCrYpT = b'ZmRhdGFfZW5jcnlwdGlvbl9rZXlfZm9yX3NlY3VyaXR5X3Rlc3RfMjAyNA=='
        
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
        x = (self.__wMnPqRtY.winfo_screenwidth() // 2) - (700 // 2)
        y = (self.__wMnPqRtY.winfo_screenheight() // 2) - (500 // 2)
        self.__wMnPqRtY.geometry(f"700x500+{x}+{y}")
    
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
        self.__hEaDeR_fRaMe = tk.Frame(self.__mAiN_fRaMe, bg='#0a0a0a', height=90)
        self.__hEaDeR_fRaMe.pack(fill='x', pady=8)
        self.__hEaDeR_fRaMe.pack_propagate(False)
        
        # Failure message with neon glow effect
        self.__fAiLuRe_LaBel = tk.Label(self.__hEaDeR_fRaMe, 
                                       text="⚠️ SECURITY ASSESSMENT FAILED ⚠️",
                                       font=('Orbitron', 24, 'bold'),
                                       fg='#ff0080',
                                       bg='#0a0a0a')
        self.__fAiLuRe_LaBel.pack(pady=20)
        
        # Subtitle
        self.__sUbTiTlE_lAbEl = tk.Label(self.__hEaDeR_fRaMe,
                                        text="USB Drop Attack Simulation - Educational Purpose",
                                        font=('Consolas', 12),
                                        fg='#00ffff',
                                        bg='#0a0a0a')
        self.__sUbTiTlE_lAbEl.pack()
        
        # Bottom section with signature (pack early to reserve space)
        self.__bOtToM_fRaMe = tk.Frame(self.__mAiN_fRaMe, bg='#0a0a0a')
        self.__bOtToM_fRaMe.pack(fill='x', side='bottom', pady=(0, 6))
        
        self.__sIgNaTuRe_LaBel = tk.Label(self.__bOtToM_fRaMe,
                                           text="By Cybersecurity Team Alignex",
                                           font=('Orbitron', 12, 'bold'),
                                           fg='#00ffff',
                                           bg='#0a0a0a')
        self.__sIgNaTuRe_LaBel.pack(side='bottom', pady=(0, 6))
        
        self.__cLoSe_BuTtOn = tk.Button(self.__bOtToM_fRaMe,
                                        text="ACKNOWLEDGE & CLOSE",
                                        font=('Orbitron', 12, 'bold'),
                                        fg='#000000',
                                        bg='#00ff00',
                                        activeforeground='#000000',
                                        activebackground='#00ffff',
                                        relief='flat',
                                        width=25,
                                        command=self.__cLoSe_ApPlIcAtIoN)
        self.__cLoSe_BuTtOn.pack(pady=(6, 0))
        
        # Content area with neon border
        self.__cOnTeNt_FrAmE = tk.Frame(self.__mAiN_fRaMe, bg='#1a1a1a', 
                                       highlightbackground='#ff0080', 
                                       highlightthickness=1, relief='solid')
        self.__cOnTeNt_FrAmE.pack(fill='both', expand=True, padx=16, pady=(6, 6))
        
        # What happened section
        self.__wHaT_hApPeNeD_lAbEl = tk.Label(self.__cOnTeNt_FrAmE,
                                             text="WHAT JUST HAPPENED?",
                                             font=('Orbitron', 16, 'bold'),
                                             fg='#00ff00',
                                             bg='#1a1a1a')
        self.__wHaT_hApPeNeD_lAbEl.pack(pady=(20, 10))
        
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
        
        self.__eXpLaNaTiOn_TeXt = tk.Text(self.__cOnTeNt_FrAmE, 
                                         font=('Consolas', 10),
                                         fg='#ffffff',
                                         bg='#2a2a2a',
                                         insertbackground='#00ffff',
                                         selectbackground='#ff0080',
                                         relief='flat',
                                         wrap='word',
                                           height=6)
        self.__eXpLaNaTiOn_TeXt.pack(fill='both', expand=False, padx=12, pady=8)
        self.__eXpLaNaTiOn_TeXt.insert('1.0', explanation_text)
        self.__eXpLaNaTiOn_TeXt.config(state='disabled')
        
        # Security tips section
        self.__tIpS_lAbEl = tk.Label(self.__cOnTeNt_FrAmE,
                                    text="🛡️ SECURITY BEST PRACTICES",
                                    font=('Orbitron', 14, 'bold'),
                                    fg='#00ff00',
                                    bg='#1a1a1a')
        self.__tIpS_lAbEl.pack(pady=(10, 5))
        
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
        self.__tIpS_tExT.pack(pady=5)
        
        # Ensure layout reserves space above the bottom frame (no-op if unsupported)
        try:
            self.__cOnTeNt_FrAmE.pack_configure(before=self.__bOtToM_fRaMe)
        except Exception:
            pass
        
        # Add decorative elements
        self.__aDd_DeCoRaTiVe_ElEmEnTs()
    
    def __aDd_DeCoRaTiVe_ElEmEnTs(self):
        corners = ['┌', '┐', '└', '┘']
        positions = [(20, 20), (660, 20), (20, 450), (660, 450)]
        
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
        
        self.__wMnPqRtY.mainloop()

# Obfuscated main execution
if __name__ == "__main__":
    # Additional obfuscation layers
    exec("".join([chr(ord(c) ^ 0) for c in "app = XvKjP9mNqR()"]))
    exec("".join([chr(ord(c) ^ 0) for c in "app.rUn_ApPlIcAtIoN()"]))

# Decryption utility (for your reference only)
"""
DECRYPTION UTILITY - FOR ADMIN USE ONLY:

To decrypt the stored data, use this function:

def decrypt_assessment_data(file_path, key=None):
    from cryptography.fernet import Fernet
    import base64
    import json
    
    if key is None:
        base_key = base64.b64decode(b'ZmRhdGFfZW5jcnlwdGlvbl9rZXlfZm9yX3NlY3VyaXR5X3Rlc3RfMjAyNA==').decode()
        key = base64.urlsafe_b64encode(base_key[:32].ljust(32, '0').encode())
    
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    return json.loads(decrypted_data.decode())

# Usage: data = decrypt_assessment_data('.sys_c2VjdXJp.dat')
"""