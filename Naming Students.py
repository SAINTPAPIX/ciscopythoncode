<html>
<head>
<title>Naming Students.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #cc7832;}
.s3 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Naming Students.py</font>
</center></td></tr></table>
<pre><span class="s0">print(</span><span class="s1">'Class Captain Randomizer'</span><span class="s0">)</span>
<span class="s0">number_of_students=int(input(</span><span class="s1">'Enter the number of students'</span><span class="s0">))</span>
<span class="s0">student_name=[]</span>
<span class="s2">for </span><span class="s0">x </span><span class="s2">in </span><span class="s0">range(number_of_students):</span>
    <span class="s0">name=str(input(</span><span class="s1">'Enter your name'</span><span class="s0">))</span>
    <span class="s0">student_name.append(name)</span>
<span class="s2">for </span><span class="s0">y </span><span class="s2">in </span><span class="s0">student_name:</span>
    <span class="s0">print(y)</span>
<span class="s0">print(student_name[</span><span class="s3">0</span><span class="s0">]</span><span class="s2">,</span><span class="s0">str(</span><span class="s1">'is the class captain'</span><span class="s0">))</span></pre>
</body>
</html>