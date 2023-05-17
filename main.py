'''
Made by KrakenDev

A program to keep track of active and unpaid licenses to websites
that KrakenDev has made for clients, in order to disable websites
that are in violation of payment agreements.
'''

import interactionManager as man
import customtkinter as CTk
import os
import dotenv

CTk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = CTk.CTk()
window.geometry("200x50")

dotenv.load_dotenv()
key = os.getenv("MASTER_TRUST_KEY")

def start():
    keyWindow = CTk.CTkToplevel(window)
    keyWindow.title("Web Licensing Protection - Master Trust Key")
    keyWindow.geometry("300x300")
    keyWindow.resizable(False, False)
    keyWindow.grab_set()
    keyWindow.focus_set()
    keyWindow.transient(window)
    keyWindow.protocol("WM_DELETE_WINDOW", lambda: keyWindow.destroy())

    keyLabel = CTk.CTkLabel(keyWindow, text="Master Trust Key:")
    keyLabel.grid(row=0, column=0)

    keyEntry = CTk.CTkEntry(keyWindow, width=100)
    keyEntry.grid(row=0, column=1)

    def submit():
        global key
        if keyEntry.get() == key:
            keyWindow.destroy()
            main()
        else:
            keyWindow.destroy()

    submitCTkButton = CTk.CTkButton(keyWindow, text="Submit", command=submit)
    submitCTkButton.grid(row=1, column=1)

startCTkButton = CTk.CTkButton(window, text="Start", command=start)
startCTkButton.grid(row=0, column=0)

output = CTk.CTkTextbox(window, width=200, height=300)

def main():
    output.grid(row=5, column=0, columnspan=3)
    window.title("Web Licensing Protection - Main")
    window.geometry("420x500")
    window.resizable(True, True)
    window.grab_set()
    window.focus_set()

    startCTkButton.destroy()

    output.delete("1.0", CTk.END)
    output.insert(CTk.END, "Code Accepted\nWelcome to the Web Licensing Protection program.\n\n")

    def add():
        addLicenseWindow = CTk.CTkToplevel(window)
        addLicenseWindow.title("Web Licensing Protection - Add License")
        addLicenseWindow.geometry("300x300")
        addLicenseWindow.resizable(False, False)
        addLicenseWindow.grab_set()
        addLicenseWindow.focus_set()
        addLicenseWindow.transient(window)
        addLicenseWindow.protocol("WM_DELETE_WINDOW", lambda: addLicenseWindow.destroy())

        AL_keyLabel = CTk.CTkLabel(addLicenseWindow, text="License Key (optional):")
        AL_keyLabel.grid(row=0, column=0)

        AL_keyEntry = CTk.CTkEntry(addLicenseWindow, width=150)
        AL_keyEntry.grid(row=0, column=1)

        AL_domainCTkLabel = CTk.CTkLabel(addLicenseWindow, text="Domain:")
        AL_domainCTkLabel.grid(row=1, column=0)

        AL_domainEntry = CTk.CTkEntry(addLicenseWindow, width=150)
        AL_domainEntry.grid(row=1, column=1)

        AL_ipAddressCTkLabel = CTk.CTkLabel(addLicenseWindow, text="IP Address:")
        AL_ipAddressCTkLabel.grid(row=2, column=0)

        AL_ipAddressEntry = CTk.CTkEntry(addLicenseWindow, width=150)
        AL_ipAddressEntry.grid(row=2, column=1)

        def AL_submit():
            try:
                man.addLicense(AL_keyEntry.get(), AL_domainEntry.get(), AL_ipAddressEntry.get())
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, "License added successfully.")
                addLicenseWindow.destroy()
            except Exception as e:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, f"Error: Could not add license.\n{e}")
                addLicenseWindow.destroy()

        submitButton = CTk.CTkButton(addLicenseWindow, text="Submit", command=AL_submit)
        submitButton.grid(row=3, column=0)

    def remove():
        removeLicenseWindow = CTk.CTkToplevel(window)
        removeLicenseWindow.title("Web Licensing Protection - Remove License")
        removeLicenseWindow.geometry("300x300")
        removeLicenseWindow.resizable(False, False)
        removeLicenseWindow.grab_set()
        removeLicenseWindow.focus_set()
        removeLicenseWindow.transient(window)
        removeLicenseWindow.protocol("WM_DELETE_WINDOW", lambda: removeLicenseWindow.destroy())

        R_keyLabel = CTk.CTkLabel(removeLicenseWindow, text="License Key:")
        R_keyLabel.grid(row=0, column=0)

        R_keyEntry = CTk.CTkEntry(removeLicenseWindow, width=150)
        R_keyEntry.grid(row=0, column=1)

        def R_submit():
            try:
                man.removeLicense(R_keyEntry.get())
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, "License removed successfully.")
                removeLicenseWindow.destroy()
            except Exception as e:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, f"Error: Could not remove license.\n{e}")
                removeLicenseWindow.destroy()

        submitButton = CTk.CTkButton(removeLicenseWindow, text="Submit", command=R_submit)
        submitButton.grid(row=1, column=0)
    
    def activate():
        activateWindow = CTk.CTkToplevel(window)
        activateWindow.title("Web Licensing Protection - Activate License")
        activateWindow.geometry("300x300")
        activateWindow.resizable(False, False)
        activateWindow.grab_set()
        activateWindow.focus_set()
        activateWindow.transient(window)
        activateWindow.protocol("WM_DELETE_WINDOW", lambda: activateWindow.destroy())

        A_keyLabel = CTk.CTkLabel(activateWindow, text="License Key:")
        A_keyLabel.grid(row=0, column=0)

        A_keyEntry = CTk.CTkEntry(activateWindow, width=100)
        A_keyEntry.grid(row=0, column=1)

        def A_submit():
            try:
                man.activateLicense(A_keyEntry.get())
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, "License activated successfully.")
                activateWindow.destroy()
            except Exception as e:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, f"Error: Could not activate license.\n{e}")
                activateWindow.destroy()

        submitButton = CTk.CTkButton(activateWindow, text="Submit", command=A_submit)
        submitButton.grid(row=1, column=0)
    
    def deactivate():
        deactivateWindow = CTk.CTkToplevel(window)
        deactivateWindow.title("Web Licensing Protection - Deactivate License")
        deactivateWindow.geometry("300x300")
        deactivateWindow.resizable(False, False)
        deactivateWindow.grab_set()
        deactivateWindow.focus_set()
        deactivateWindow.transient(window)
        deactivateWindow.protocol("WM_DELETE_WINDOW", lambda: deactivateWindow.destroy())

        D_keyLabel = CTk.CTkLabel(deactivateWindow, text="License Key:")
        D_keyLabel.pack()

        D_keyEntry = CTk.CTkEntry(deactivateWindow, width=100)
        D_keyEntry.pack()

        def D_submit():
            try:
                man.deactivateLicense(D_keyEntry.get())
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, "License deactivated successfully.")
                deactivateWindow.destroy()
            except Exception as e:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, f"Error: Could not deactivate license.\n{e}")
                deactivateWindow.destroy()

        submitButton = CTk.CTkButton(deactivateWindow, text="Submit", command=D_submit)
        submitButton.pack()

    def get():
        getWindow = CTk.CTkToplevel(window)
        getWindow.title("Web Licensing Protection - Get License")
        getWindow.geometry("300x300")
        getWindow.resizable(False, False)
        getWindow.grab_set()
        getWindow.focus_set()
        getWindow.transient(window)
        getWindow.protocol("WM_DELETE_WINDOW", lambda: getWindow.destroy())

        G_domainLabel = CTk.CTkLabel(getWindow, text="Domain:")
        G_domainLabel.pack()

        G_domainEntry = CTk.CTkEntry(getWindow, width=100)
        G_domainEntry.pack()

        def G_submit():
            try:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, man.getLicense(G_domainEntry.get()))
                getWindow.destroy()
            except Exception as e:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, f"Error: Could not retrieve license.\n{e}")
                getWindow.destroy()

        submitButton = CTk.CTkButton(getWindow, text="Submit", command=G_submit)
        submitButton.pack()

    def getInfo():
        getInfoWindow = CTk.CTkToplevel(window)
        getInfoWindow.title("Web Licensing Protection - Get License Info")
        getInfoWindow.geometry("300x300")
        getInfoWindow.resizable(False, False)
        getInfoWindow.grab_set()
        getInfoWindow.focus_set()
        getInfoWindow.transient(window)
        getInfoWindow.protocol("WM_DELETE_WINDOW", lambda: getInfoWindow.destroy())

        GI_keyCTkLabel = CTk.CTkLabel(getInfoWindow, text="License Key:")
        GI_keyCTkLabel.pack()

        GI_keyEntry = CTk.CTkEntry(getInfoWindow, width=100)
        GI_keyEntry.pack()

        def GI_submit():
            try:
                output.delete("1.0", CTk.END)
                LI = man.getLicenseInfo(GI_keyEntry.get())
                # Put the tuple into a list
                LI = list(LI)
                if LI[1] == 1:
                    LI[1] = "Activated"
                elif LI[1] == 0:
                    LI[1] = "Deactivated"
                else:
                    LI[1] = "Unknown/NaN"
                LI_names = ["License Key", "Activation Status", "Domain", "IP Address"]
                for i in range(len(LI)):
                    output.insert(CTk.END, f"{LI_names[i]}: ")
                    output.insert(CTk.END, f"{LI[i]}\n\n")
                getInfoWindow.destroy()
            # Check if the license key is invalid, aka, None.
            except TypeError:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, "Error: Invalid license key.")
                getInfoWindow.destroy()
            except Exception as e:
                output.delete("1.0", CTk.END)
                output.insert(CTk.END, f"Error: Could not retrieve license info.\n{e}")
                getInfoWindow.destroy()

        submitButton = CTk.CTkButton(getInfoWindow, text="Submit", command=GI_submit)
        submitButton.pack()

    addLicenseButton = CTk.CTkButton(window, text="Add License", command=add)
    addLicenseButton.grid(row=0, column=0)

    removeLicenseButton = CTk.CTkButton(window, text="Remove License", command=remove)
    removeLicenseButton.grid(row=0, column=1)

    activateLicenseButton = CTk.CTkButton(window, text="Activate License", command=activate)
    activateLicenseButton.grid(row=0, column=2)

    deactivateLicenseButton = CTk.CTkButton(window, text="Deactivate License", command=deactivate)
    deactivateLicenseButton.grid(row=1, column=0)

    getLicenseButton = CTk.CTkButton(window, text="Get License", command=get)
    getLicenseButton.grid(row=1, column=1)

    getLicenseInfoButton = CTk.CTkButton(window, text="Get License Info", command=getInfo)
    getLicenseInfoButton.grid(row=1, column=2)

window.mainloop()