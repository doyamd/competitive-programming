<h2><a href="https://leetcode.com/problems/crawler-log-folder/">1598. Crawler Log Folder</a></h2><h3>Easy</h3><hr><div><p _msttexthash="4746534" _msthash="21">The Leetcode file system keeps a log each time some user performs a <em>change folder</em> operation.</p>

<p _msttexthash="914810" _msthash="22">The operations are described below:</p>

<ul>
	<li><code>"../"</code><font _mstmutation="1" _msttexthash="6916845" _msthash="23"> : Move to the parent folder of the current folder. (If you are already in the main folder, <strong _mstmutation="1">remain in the same folder</strong>).</font></li>
	<li><code>"./"</code><font _mstmutation="1" _msttexthash="540527" _msthash="24"> : Remain in the same folder.</font></li>
	<li><code>"x/"</code><font _mstmutation="1" _msttexthash="3288974" _msthash="25"> : Move to the child folder named  (This folder is <strong _mstmutation="1">guaranteed to always exist</strong>).</font><code>x</code></li>
</ul>

<p><font _mstmutation="1" _msttexthash="4253275" _msthash="26">You are given a list of strings  where  is the operation performed by the user at the  step.</font><code>logs</code><code>logs[i]</code><code>i<sup>th</sup></code></p>

<p><font _mstmutation="1" _msttexthash="3653104" _msthash="27">The file system starts in the main folder, then the operations in  are performed.</font><code>logs</code></p>

<p _msttexthash="6891846" _msthash="28">Return <em>the minimum number of operations needed to go back to the main folder after the change folder operations.</em></p>

<p>&nbsp;</p>
<p><strong class="example" _msttexthash="114439" _msthash="29">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png" style="width: 775px; height: 151px;"></p>

<pre><strong>Input:</strong> logs = ["d1/","d2/","../","d21/","./"]
<strong>Output:</strong> 2
<strong>Explanation: </strong>Use this change folder operation "../" 2 times and go back to the main folder.
</pre>

<p><strong class="example" _msttexthash="114621" _msthash="30">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png" style="width: 600px; height: 270px;"></p>

<pre><strong>Input:</strong> logs = ["d1/","d2/","./","d3/","../","d31/"]
<strong>Output:</strong> 3
</pre>

<p><strong class="example" _msttexthash="114803" _msthash="31">Example 3:</strong></p>

<pre><strong>Input:</strong> logs = ["d1/","../","../","../"]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong _msttexthash="199901" _msthash="32">Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>3</sup></code></li>
	<li><code>2 &lt;= logs[i].length &lt;= 10</code></li>
	<li><code>logs[i]</code><font _mstmutation="1" _msttexthash="1592604" _msthash="33"> contains lowercase English letters, digits, , and .</font><code>'.'</code><code>'/'</code></li>
	<li><code>logs[i]</code><font _mstmutation="1" _msttexthash="1442506" _msthash="34"> follows the format described in the statement.</font></li>
	<li _msttexthash="2378740" _msthash="35">Folder names consist of lowercase English letters and digits.</li>
</ul>
</div>