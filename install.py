import sys, os, subprocess, platform, shutil
if platform.system()!="Linux" and not ("--ignore-os" in sys.argv):
  print("This program is only available on Linux",file=sys.stderr)
  print("Use the --ignore-os argument to ignore this error",file=sys.stderr)
  sys.exit(1)
os.chdir(os.path.dirname(__file__))
if platform.system()=="Linux":
  if shutil.which("apt")!=None and shutil.which("trans")==None:
    subprocess.Popen(["apt","install","-y","--no-install-recommends","--no-install-suggests","translate-shell"]).wait()
subprocess.Popen([sys.executable,"-m","pip","install","-U","requirements.txt"]).wait()
if shutil.which("trans")==None:
  print('"trans" command not found',file=sys.stderr)
  print('Install the "translate-shell" program',file=sys.stderr)
  print("https://github.com/soimort/translate-shell",file=sys.stderr)
  sys.exit(2)