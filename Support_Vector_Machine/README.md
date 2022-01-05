# Support Vector Machines

<p>
    Support vector machines are a common method used for classification problemas,<br>
    The have been proven.
</p>

# Cutting data with style
<p>
 the line must to stay very closer to all possibles points on the graph.
</p>

# Maximizing the Margin
<h2> Minimizing the Error </h2>
<p>
    ERROR = CLASSIFICATION + MARGIN ERROR
</p>

# Perceptron Algorithm

# Classification Error
<div>
    <p> equantion of line is :<br>
        wx + b = 0
    </p>
    <p>
        In this case we will need two extra lines that create the margin.<br>
        so, we will have something like this:<br>
        positive (margin top line)      Wx + b = 1 <br>
        middle  (line)                  Wx + b = 0  <br>
        negative  (margin bottom line)  Wx + b = -1 <br>
        <b>Step 2</b><br>
        split in twice <br>
        the blue error starts from the bottom line and the red error<br>
        starts from the top line<br>
        now we look at values of Wx + b<br>
        <b> example </b><br>
        blue error = 1.5, 3.5, 0.5 <br>
        red error  = 2 + 3 + 0.3 <br>
        Error = 1.5 + 3.5 + 0.5 + 2 + 3 + 0.3 = 10.8
    </p>
</div>

# Margin Error

<div>
    <img style="width:auto;" src="img/margin_error.png" alt="margin_error" >
    <img style="width:auto;" src="img/margin_error1.png" alt="margin_error1" >
    <img style="width:auto;" src="img/margin_error2.png" alt="margin_error2" >
</div>

# Error Function
<div>
    <p>
        Error = Classification Error + Margin Error<br>
        <b>Minimize using gradient descent</b>
    </p>
    <h3> The C Paramenter </h3>
    <p> 
    The C parameter is just a constant that attacges itself to the classification error.<br>
    Error = C classification Error + Margin Error<br>
    Large C: Focus on classifying points<br>
    Small C: Focurs on a large margin<br>
    </p>
</div>

# Polymonial Kernel

<div>
    <img style="width:auto;" src="img/kernel_trick.png" alt="kernel_trick" >
    <img style="width:auto;" src="img/kernel_trick1.png" alt="kernel_trick1" >
    <img style="width:auto;" src="img/kernel_trick2.png" alt="kernel_trick2" >
</div>

# recap

<div>
    <p>
        In this lesson, you learned about Support Vector Machines (or SVMs).<br>
        SVMs are a popular algorithm used for classification problems. You saw <br>
        three different ways that SVMs can be implemented:</p>
    <ol>
        <li> Maximum Margin Classifier </li>
        <p>
            When your data can be completely separated, the linear version of <br>
            SVMs attempts to maximize the distance from the linear boundary to the <br>
            closest points (called the support vectors). For this reason, we saw that <br>
            in the picture below, the boundary on the left is better than the one on the <br>
            right.
        </p>
        <li> Classification with Inseparable Classes </li>
        <p>
            Unfortunately, data in the real world is rarely completely separable as shown<br>
            in the above images. For this reason, we introduced a new hyper-parameter called C.<br>
            The C hyper-parameter determines how flexible we are willing to be with the points that<br>
            fall on the wrong side of our dividing boundary. The value of C ranges between 0 and infinity.<br>
            When C is large, you are forcing your boundary to have fewer errors than when it is a small value.
        </p>
        <li> Kernel Methods </li>
        <p>
            By far the most popular kernel is the rbf kernel (which stands for radial basis function). <br>
            The rbf kernel allows you the opportunity to classify points that seem hard to separate in any space. <br>
            This is a density based approach that looks at the closeness of points to one another. This introduces<br>
            another hyper-parameter gamma. When gamma is large, the outcome is similar to having a large value of C, <br>
            that is your algorithm will attempt to classify every point correctly. Alternatively, small values of gamma <br>
            will try to cluster in a more general way that will make more mistakes, but may perform better when it sees new data.
        <p>
    <ol>
</div>
