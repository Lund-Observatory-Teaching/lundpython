---
layout: default
title: "LundPython"
---
<style>
intro {
	max-width: 14cm;
    height= 20cm;
    border: 0px;
}
div.vertical-line{
	width: 0px; /* Use only border style */
	height: 100%;
	float: right;
    opacity: 40%;
	border: 1px inset; /* This is default border style for <hr> tag */
    margin-right: 0.4cm;
    margin-left: 0.4cm;
    margin-top: 0.4cm;
}
#myBtn {
  font-size: 18px;
  border: none;
  outline: none;
  background-color: green;
  color: white;
  cursor: pointer;
  padding: 15px;
  border-radius: 4px;
  width: 4cm;
}

#myBtn:hover {
  background-color: #555;
}
</style>
<script>
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
</script>
<h1><center>Your teachers </center></h1><br>

<intro>
    <img align=left width=300 src="imgs/eero.jpeg">
    <div class="vertical-line" style="height: 11.3cm; float:left"></div>
    <h1 style="margin-top:-0.3cm">Eero Vaher</h1>
    Eero Vaher started his PhD at Lund Observatory in 2019 under the supervision of Drs David Hobbs & Paul McMillan.
    His research is focused on the <i>Gaia</i> bright reference frame.<br>
    <br>
    He is an Astropy contributor and has been involved in the Python programming course since 2020.
    He is aiming to help the students write code that not only works, but is also short, simple and maintainable.
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
</intro>
<br>

<intro>
	<img align="right" src="imgs/simon.jpeg" width=300>
    <div class="vertical-line" style="height: 11.3cm;"></div>
    <h1 style="margin-top:-0.3cm">Simon Alinder</h1>
    Simon Alinder started his PhD at Lund observatory in 2021, supervised by Drs Thomas Bensby and Paul McMillan, and is researching galactic archeology and the Gaia Phase spiral.<br>
    <br>
    Simon joined the teachers of the Python programming course in 2021 to help make sure the students Lund Observatory are able to carry out their own computations and analyses.
</intro>
<br><br><br><br><br><br><br><br>
<center><button class="btn-default" onclick="topFunction()" id="myBtn" title="Go to top">Go to top</button><center>
