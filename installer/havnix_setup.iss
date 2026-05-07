; Havnix Setup Script for Inno Setup
; Creates a professional Windows installer (setup.exe)
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
WizardStyle=modern
SetupIconFile=..\website\assets\images\logo.ico

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create Havnix desktop shortcut"; GroupDescription: "Additional shortcuts:"
Name: "desktopicon_ide"; Description: "Create Havnix IDE desktop shortcut"; GroupDescription: "Additional shortcuts:"
Name: "addtopath"; Description: "Add Havnix to system PATH"; GroupDescription: "System integration:"; Flags: checkedonce
Name: "fileassoc"; Description: "Associate .havnix files with Havnix"; GroupDescription: "System integration:"; Flags: checkedonce

[Files]
; Core files
Source: "..\havnix.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\ide.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\GUIDE.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\HOW_TO_RUN.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\core\*"; DestDir: "{app}\core"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\packages\*"; DestDir: "{app}\packages"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\examples\*"; DestDir: "{app}\examples"; Flags: ignoreversion recursesubdirs createallsubdirs

; Pre-built executables (if they exist - build with build_installer.bat first)
Source: "..\dist\havnix.exe"; DestDir: "{app}"; Flags: ignoreversion skipifsourcedoesntexist
Source: "..\dist\havnix-ide.exe"; DestDir: "{app}"; Flags: ignoreversion skipifsourcedoesntexist

; Batch wrappers (fallback if exe not built)
Source: "..\run_ide.bat"; DestDir: "{app}"; Flags: ignoreversion

[Dirs]
Name: "{app}\havnix_libraries"

[Icons]
; Start Menu
Name: "{group}\Havnix IDE"; Filename: "{app}\havnix-ide.exe"; WorkingDir: "{app}"; Comment: "Havnix IDE"; Check: FileExists(ExpandConstant('{app}\havnix-ide.exe'))
Name: "{group}\Havnix IDE"; Filename: "python"; Parameters: """{app}\ide.py"""; WorkingDir: "{app}"; Comment: "Havnix IDE"; Check: not FileExists(ExpandConstant('{app}\havnix-ide.exe'))
Name: "{group}\Havnix Guide"; Filename: "{app}\GUIDE.md"
Name: "{group}\Havnix Examples"; Filename: "{app}\examples"
Name: "{group}\Uninstall Havnix"; Filename: "{uninstallexe}"

; Desktop shortcuts (optional)
Name: "{userdesktop}\Havnix"; Filename: "{app}\havnix.exe"; WorkingDir: "{app}"; Comment: "Havnix"; Tasks: desktopicon; Check: FileExists(ExpandConstant('{app}\havnix.exe'))
Name: "{userdesktop}\Havnix IDE"; Filename: "{app}\havnix-ide.exe"; WorkingDir: "{app}"; Comment: "Havnix IDE"; Tasks: desktopicon_ide; Check: FileExists(ExpandConstant('{app}\havnix-ide.exe'))
Name: "{userdesktop}\Havnix IDE"; Filename: "python"; Parameters: """{app}\ide.py"""; WorkingDir: "{app}"; Comment: "Havnix IDE"; Tasks: desktopicon_ide; Check: not FileExists(ExpandConstant('{app}\havnix-ide.exe'))

[Registry]
; Add to PATH (optional task)
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Tasks: addtopath; Check: NeedsAddPath('{app}')

; File association (optional task)
Root: HKCR; Subkey: ".havnix"; ValueType: string; ValueData: "HavnixFile"; Flags: uninsdeletevalue; Tasks: fileassoc
Root: HKCR; Subkey: "HavnixFile"; ValueType: string; ValueData: "Havnix Source File"; Flags: uninsdeletekey; Tasks: fileassoc
Root: HKCR; Subkey: "HavnixFile\shell\open\command"; ValueType: string; ValueData: "python ""{app}\havnix.py"" ""%1"""; Tasks: fileassoc
Root: HKCR; Subkey: "HavnixFile\shell\edit"; ValueType: string; ValueData: "Open in Havnix IDE"; Tasks: fileassoc
Root: HKCR; Subkey: "HavnixFile\shell\edit\command"; ValueType: string; ValueData: "python ""{app}\ide.py"""; Tasks: fileassoc

[Run]
Filename: "python"; Parameters: "-m pip install -r ""{app}\requirements.txt"" --quiet"; StatusMsg: "Installing dependencies..."; Flags: runhidden; Check: PythonExists
Filename: "{app}\havnix-ide.exe"; Description: "Launch Havnix IDE"; Flags: postinstall nowait skipifsilent; Check: FileExists(ExpandConstant('{app}\havnix-ide.exe'))
Filename: "python"; Parameters: """{app}\ide.py"""; Description: "Launch Havnix IDE"; Flags: postinstall nowait skipifsilent; Check: not FileExists(ExpandConstant('{app}\havnix-ide.exe'))

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

function PythonExists(): boolean;
var
  ResultCode: Integer;
begin
  Result := Exec('python', '--version', '', SW_HIDE, ewWaitUntilTerminated, ResultCode) and (ResultCode = 0);
end;
