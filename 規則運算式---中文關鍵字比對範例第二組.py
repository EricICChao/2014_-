import re
print(re.search(r"[了][發]","ab我是bbb發了123"))
print(re.search(r"[發][了]","ab我是bbb發了123"))
print(re.search(r"[發了]","ab我是bbb發了123"))
print(re.search(r"[了發]","ab我是bbb發了123"))
print(re.search(r"[發][了]","ab我是bbb發123"))
print(re.search(r"[了][發]","ab我是bbb發123"))
print(re.search(r"[了發]","ab我是bbb發123"))
print(re.search(r"[發],[了]","ab我是bbb發123"))

print(re.findall(r"[發了]", "ji35k4c我這回了發了發了發了發了發,了發  了發__了發"))
print(re.findall(r"\b發了\b", "ji35k4c我這回了發了發了發了發了發,了發  了發__了發"))
print(re.findall(r"[發了]", "ji35k4c我這回了發了發了發了發了發,了發  了發__了發"))
print(re.findall(r"[\b發了\b]", "我這回了發了發了發了發了發,了發  了發__了發"))
print(re.findall(r"[907f][96e3]", "避難、去避難囉、安安我避難了避難了避難了避難了難避難了"))
print(re.findall(r"(?u)\b發了\b", "我這回了發了發了發了發了發,了發  了發__了發"))




print(re.findall(r"[\u907f][\u96e3]", "避難、去避難囉、安安我避難了避難了避難了避難了難避難了"))

print(re.findall(r"\b[\u907f][\u96e3]\b", "避難、去避難囉、安安我避難了避難了避難了避難了難避難了"))

a = re.findall(r"[\u907f][\u96e3]", "避難、去避難囉、安安我避難了避難了避難了避難了難避難了")
print(a.count("避難"))


c = "避難、去避難囉、安安我避難了避難了避難了避難了難避難了"
print(c.count("避難"))


print(re.findall(r"[避][難]", "避難、去避難囉、安安我避難了避難了避難了避難了難避難了"))
print(re.findall(r"[避難]", "避難、去避難囉、安安我避難了避難了避難了避難了難避難了"))
