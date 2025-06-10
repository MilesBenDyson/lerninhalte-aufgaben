# 🚀 Git Upload Anleitung

## 📌 Zweck

Diese Anleitung hilft dir dabei, ein **lokales Git-Repository mit GitHub zu verbinden** und es korrekt hochzuladen (inkl. moderner `main`-Branch).

---

## 📝 1️⃣ Repository auf GitHub anlegen

👉 Gehe zu [github.com](https://github.com)  
👉 Klicke oben rechts auf **New repository**  
👉 Repository Name z.B.: `lern-zertifikate`  
👉 Keine README anlegen (du hast sie lokal)  
👉 **URL merken → SSH bevorzugt:**  
`git@github.com:DEINUSERNAME/lern-zertifikate.git`

---

## 🗂️ 2️⃣ Lokales Repository vorbereiten

👉 Öffne **Git Bash**, wechsle in deinen Ordner:

```bash
cd /Pfad/zum/Ordner
````

Beispiel:

```bash
cd ~/Desktop/Projekte/lern-zertifikate
```

👉 Git initialisieren:

```bash
git init
```

---

## 📋 3️⃣ Dateien zum Staging hinzufügen

```bash
git add .
git status     # Kontrolle: alle Dateien ready?
```

---

## ✍️ 4️⃣ Ersten Commit machen

```bash
git commit -m "Initial commit: Lernzertifikate hinzugefügt"
```

---

## 🌿 5️⃣ Branch korrekt setzen (`main` statt `master`)

```bash
git branch -M main
```

---

## 🌐 6️⃣ Remote hinzufügen → Verbindung zu GitHub

```bash
git remote add origin git@github.com:DEINUSERNAME/lern-zertifikate.git
```

---

## 🚀 7️⃣ Repo hochladen (erster Push)

git push -u origin main
```

---

## 🎉 Kontrolle

👉 Öffne dein Repository auf GitHub → deine Dateien sollten sichtbar sein.

---

### Merksatz:

👉 **`git init` → `add` → `commit` → `branch -M main` → `remote add` → `push`**

---

## 💡 Hinweis

👉 `main` = moderner Name für den Hauptbranch
👉 `master` = alter Name → technisch gleich, aber nicht mehr Standard

---

**© 2025 Ben (MilesBenDyson) — Git Upload Guide**

````

