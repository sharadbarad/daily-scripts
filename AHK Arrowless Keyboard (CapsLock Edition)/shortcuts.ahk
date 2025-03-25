#UseHook 					           ; Ensures that the hotkeys work properly
#Requires AutoHotkey v2.0 	 ; Ensures that this file needs v2.0 to work properly
#Warn All, Off
#SingleInstance Force

CapsLock & i::
{
SendInput("{Blind}{Up}")
}

CapsLock & k::
{
SendInput("{Blind}{Down}")
}

CapsLock & j::
{
SendInput("{Blind}{Left}")
}

CapsLock & l::
{
SendInput("{Blind}{Right}")
}

CapsLock & `;::
{
SendInput("{Blind}{Right}")
}

CapsLock & p::
{
SendInput("{Blind}{PrintScreen}")
}

CapsLock & Backspace::
{
SendInput("{Blind}{Delete}")
}


; Define hotkeys for media controls
CapsLock & 1::Send("{Volume_Mute}")  ; Mute
CapsLock & 2::Send("{Volume_Down}")  ; Volume Decrease
CapsLock & 3::Send("{Volume_Up}")    ; Volume Increase



