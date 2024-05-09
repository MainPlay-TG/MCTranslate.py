from MainShortcuts.MainCore import ms, _MainCore
from progressbar import ProgressBar, Percentage, Bar, ETA
mcore = _MainCore(__name__=__name__, __file__=__file__)
cprint = mcore.cprint
cformat = mcore.cformat
args = ["trans", "-b", "-no-warn", "-no-autocorrect", "en:ru"]
w = [
    Percentage(),
    Bar(marker="█", fill="░", left="⟨", right="⟩"),
    ETA()
]
with open("en_US.lang", "r") as f:
  textEN = f.read().rstrip()
linesEN = textEN.split("\n")
try:
  with open("ru_RU.lang", "r") as f:
    textRU = f.read().rstrip()
  linesRU = textRU.split("\n")
except:
  linesRU = []
dictEN = {}
dictRU = {}
for i in linesEN:
  i = i.strip()
  if (not i.startswith("#")) and (i != "") and ("=" in i):
    k = i.split("=")[0]
    v = i[len(k) + 1:]
    dictEN[k.strip()] = v.strip()
for i in linesRU:
  i = i.strip()
  if (not i.startswith("#")) and (i != "") and ("=" in i):
    k = i.split("=")[0]
    v = i[len(k) + 1:]
    dictRU[k.strip()] = v.strip()
keys = []
for k in dictEN:
  if not k in dictRU:
    keys.append(k)
c = 0
pbar = ProgressBar(maxval=len(linesEN), widgets=w).start()
for k in keys:
  for i in range(3):
    try:
      result = ms.proc.run(args + [dictEN[k]])["o"].strip()
      if result != "":
        dictRU[k] = result
        break
    except:
      pass
  c += 1
  pbar.update(c)
linesRU = []
for k, v in dictRU.items():
  linesRU.append(k + "=" + v)
pbar.finish()
ms.file.write("ru_RU.lang", "\n".join(linesRU))
