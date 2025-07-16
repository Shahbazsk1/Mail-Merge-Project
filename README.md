# Mail-Merge-Project
<h2>To automatically generate personalized letters for a list of people by replacing a placeholder ([name]) in a template letter with each real name from a list.</h2>
<h3>🧱 How It Works:</h3>
<ul>
  <li>✅ You have a template letter in starting_letter.txt with [name] as a placeholder.</li>
  <li>✅ A file invited_name.txt contains a list of names — one per line.</li>
  <li>✅ The program reads both files and replaces [name] with each person’s name.</li>
  <li>✅ It saves the new personalized letters to ./Output/ReadyToSend/letter_for_<name>.docx.</li>
</ul>
<h3>🗂️ Folder Structure</h3>
<p>Project/<br>
├── Input/<br>
│   ├── Letter/<br>
│   │   └── starting_letter.txt<br>
│   └── Names/<br>
│       └── invited_name.txt<br>
├── Output/<br>
│   └── ReadyToSend/<br>
│       └── letter_for_<name>.docx<br>
├── main.py</p><br>
<h3>🔤 Example</h3>
<p>🔹 starting_letter.txt</p>
<p>Dear [name],<br>

You are invited to my birthday party this Saturday.<br>

Sincerely,<br>
Shahbaz</p>
<h3>🔹 invited_name.txt</h3>
<p>friend name1</p>
<p>friend name2</p>
<p>friend name3</p>
<h3>🔹 Output files:</h3>
<ul>
  <li>letter_for_Ali.docx</li>
  <li>letter_for_Riya.docx</li>
  <li>letter_for_Dev.docx</li>
  <p>Each letter will replace [name] with the correct person’s name.</p>
</ul>
<h3>📦 Python Module Used</h3>
<ul>
  <li><b>1. ✅ open() –</b>b> Built-in function
  <ul>
    <li>Used to read and write files (text and docx files)</li>
    <li>readlines() reads a list of names</li>
    <li>read() reads the letter content</li>
    <li>write() saves the personalized version</li>
    <p>with open("file.txt") as f:<bR>
      content = f.read()</p>
  </ul>
  </li>
</ul>
