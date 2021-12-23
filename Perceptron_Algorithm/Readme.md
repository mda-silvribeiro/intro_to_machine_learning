<div>
<title><b>
    Perceptron Algorithm
</title><br>
<h4>
    The perceptron algorithm is an algorithm for classifying data.<br>
    It's the building block of neural
</h4>
<h3 style="color:green;">
    Classification Algorithm
</h3>
<h5><b>
    For example
</b></h5>
<p>
    Is this email spam or not?<br>
    Would this user download an app or not?<br>
    Is this patient sick or not?
</p>
</div>
<div>
<h1><b>
    Classification Problems
</b><h1>
<p>
    We'll start by defining what we mean by classification problems,<br>
    and applying it to a simple example.
</p>
<h1> Quiz #1 </h1>
<img style="width:auto;" src="img/parameters.png" alt="parameters" >
<h5 style="color:red;">
    The red points to students that got rejected.
</h5>
<h5 style="color:blue;">
    The blue points to students that got accepted.
</h5>
<img style="width:auto;" src="img/graph.png" alt="graph">
</div>
<div>
<h1><b>
    Higher Dimensions
</b></h1>
    <img style="width:auto;" src="img/higher_dimensions.png" alt="hdimensions" >
</div>
<div>
<h1><b>
    Perceptron
</b></h1>
    <img style="width:auto;" src="img/perceptron0.png" alt="perceptron" >
    <img style="width:auto;" src="img/perceptron1.png" alt="perceptron" >
    <img style="width:auto;" src="img/perceptron2.png" alt="perceptron" >
    <img style="width:auto;" src="img/perceptron3.png" alt="perceptron" >
    <img style="width:auto;" src="img/perceptron4.png" alt="perceptron" >
</div>
<div>
<h1><b>
    Perceptron as Logical Operators
</b></h1>
<p>
    In this lesson, we'll see one of the many great applications of perceptrons. <br>
    As logical operators! You'll have the chance to create the perceptrons for the most<br>
    common of these, the <b>AND</b>, <b>OR</b>, and <b>NOT</b> operators. And then, we'll see what to do about <br>
    the elusive <b>XOR</b> operator. Let's dive in!
</p>
    <img style="width:auto;" src="img/perceptron5.png" alt="perceptron" >
</div>
<div>
<h1><b>
    Perceptron Algorithm Trick
</b></h1>
<p>
    n the last section you used your logic and your mathematical knowledge to create <br>
    perceptrons for some of the most common logical operators. In real life, though, <br>
    we can't be building these perceptrons ourselves. The idea is that we give them <br>
    the result, and they build themselves. For this, here's a pretty neat trick that<br>
    will help us.
    <link rel="" href="Perceptron_Algorithm/PerceptronsAsLogicalOperators.ipynb">
</p>
<h3><b>
    Time for some math!
</b></h3>
<p>
    Now that we've learned that the points that are misclassified, want the line <br>
    to move closer to them, let's do some math. The following video shows a mathematical<br>
     trick that modifies the equation of the line, so that it comes closer to a particular point.
</p>
    <img style="width:auto;" src="img/algorithm_trick.png" alt="algorithm_trick" >
    <h6 style="color:red;"> move closer to the red point</h6>
    <img style="width:auto;" src="img/algorithm_trick1.png" alt="algorithm_trick" >
    <h6 style="color:red;"> move closer to the blue point </h6>
    <img style="width:auto;" src="img/algorithm_trick2.png" alt="algorithm_trick" >
</div>

<div>
<h1>
    Correct Answers
</h1>
<ul>
    <li> Quiz #1 (Yes)</li>
    <img style="width:auto;" src="img/quiz1.png" alt="quiz1">
    <p><strong> How do we find this line? </strong></p>
    <img style="width:auto;" src="img/explanation.png" alt="exp">
</ul>
</div>
