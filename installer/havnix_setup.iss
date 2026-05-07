; Havnix Setup Script for Inno Setup
; Creates a proper Windows installer (setup.exe)
; Download Inno Setup from: https://jrsoftware.org/isinfo.php

[Setup]
AppName=Havnix
AppVersion=2.0.0
AppPublisher=Osman Salih (Snixrs)
AppPublisherURL=https://github.com/Snixrs/Havnix-Language
AppSupportURL=https://github.com/Snixrs/Havnix-Language/issues
DefaultDirName={autopf}\Havnix
DefaultGroupName=Havnix
OutputBaseFilename=havnix-setup
Compression=lzma2
SolidCompression=yes
ChangesEnvironment=yes
PrivilegesRequired=admin
UninstallDisplayName=Havnix Programming Language
LicenseFile=..\LICENSE

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\havnix.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\ide.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\GUIDE.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\HOW_TO_RUN.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\core\*"; DestDir: "{app}\core"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\packages\*"; DestDir: "{app}\packages"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\examples\*"; DestDir: "{app}\examples"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\run_ide.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\run_ide.sh"; DestDir: "{app}"; Flags: ignoreversion

[Dirs]
Name: "{app}\havnix_libraries"

[Icons]
Name: "{group}\Havnix IDE"; Filename: "python"; Parameters: """{app}\ide.py"""; WorkingDir: "{app}"; Comment: "Havnix IDE"
Name: "{group}\Havnix Guide"; Filename: "{app}\GUIDE.md"
Name: "{group}\Havnix Examples"; Filename: "{app}\examples"
Name: "{group}\Uninstall Havnix"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Havnix IDE"; Filename: "python"; Parameters: """{app}\ide.py"""; WorkingDir: "{app}"; Comment: "Havnix IDE"

[Registry]
; Add to PATH
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsAddPath('{app}')

; File association for .havnix files
Root: HKCR; Subkey: ".havnix"; ValueType: string; ValueData: "HavnixFile"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "HavnixFile"; ValueType: string; ValueData: "Havnix Source File"; Flags: uninsdeletekey
Root: HKCR; Subkey: "HavnixFile\shell\open\command"; ValueType: string; ValueData: "python ""{app}\havnix.py"" ""%1"""
Root: HKCR; Subkey: "HavnixFile\shell\edit\command"; ValueType: string; ValueData: "python ""{app}\ide.py"""

[Run]
Filename: "python"; Parameters: "-m pip install -r ""{app}\requirements.txt"""; StatusMsg: "جاري تثبيت المتطلبات..."; Flags: runhidden
Filename: "python"; Parameters: """{app}\ide.py"""; Description: "فتح Havnix IDE"; Flags: postinstall nowait skipifsilent

[UninstallRun]
Filename: "python"; Parameters: "-c ""import sys; print('Havnix uninstalled')"""; Flags: runhidden

[Code]
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKLM, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', OrigPath) then
  begin
    Result := True;
    exit;
  end;
  Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
end;
