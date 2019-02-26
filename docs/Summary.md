The over all idea of the paper is summarized here:


**i.)CLUSTERING EDGES**:
First , we take a ground truth boundary image, and from this image we select patches of say size **pxp**. For each patch we calculate the distance of its centre to the nearest edge pixel and based on a criteria we classify them as belonging to either background or non background(containing edges).This criteria is dictated interms of (d,&#952;), where d represents distance of patch from centre ,and &#952; represents orientation of the edge pixel. 

**ii.)Oriented Edge Forest** 

**a.)** To facilitate this process we make a 2D array and bin the values of **(d,&#952;)** into a 2D matrix, for different values of possible (d,&#952;) each patch can take.So we denote **'n'** different **'d'** (columns of matrix taken as 15 in paper) and **'m'** different **'&#952;'**(rows of matrix taken as 8). This gives us a matrix of 120 pairs of (d,&#952;), to which any of the patches of the image must fall. At the end of this process we would have a mapping of each patch of the ground truth boundary image to one of the 'mxn pairs'.

**b.)** Now comes the training part, where the mappings of each patch is used to train a Random forest classifier.So the patches act as data and the value in the (d,&#952;) pair for that patch acts as the class. So we would have the Random forest classifers acting as **'K'** class classifers were **'K=mxn'**. We then start testing random patches of test image, to decide the label set or the possible edge patterns existing in that patch.Certain Specifications about how the images should be represented when training, how the class labels are used all will also have to be taken care off .

**c.)** The rest of the procedure is left with coming up with methods on combining the outputs of the different decision trees for each of the image patch.Since Random Forest Classifier is nothing but an ensemble of Decision Trees. Here there are few steps that help imrpve the prediction accuracy like  **Calibration**


**iv.)Edge Fusion** 

So after applying the Random Forest Classifier on the Images we wil be left with the probability values that are calibrated.The probability of boundary at a given location is necessarily determined by the tree predictions over an entire neighborhood around that location.This step is typically to resolve these probabilities into a single, coherent image of boundary strengths.The end result will be an oriented signal E(x, y, θ) that specifies the probability of boundary at location (x, y) in the binned direction θ.

a.)The catch here is that,we are restricting our detector to capture only oriented(straight) line edges and its statistics.The classifier would fail incase of complex curved edges, or even in the case when the size of the patch increases, there are chances of the edges captured by the region to be curvy.

