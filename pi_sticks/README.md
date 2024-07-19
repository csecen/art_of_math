### Pi Sticks

#### This function uses a unique method to estimate the value of pi. The method, known as pi toss, uses equally spaced vertical lines on a plane. Then a large sample size of lines, shorter in length than the distance between the vertical lines, are randomly dropped onto the plane. Following this, the total number of lines times the length times 2 is divided by the distance between the vertical lines times the number of lines that intersect with the vertical lines. This should roughly estimate the value of pi. Repeating this procedure will should help to converage toward the value of pi. The formula is shown below.

$$ pi \approx 2 * stick length * \# tossed \over spacing * \# intersections $$

#### The following is an example call and output for the pi_sticks function:

    python art_of_math.py pi_sticks/config.json

#### The below example shows the contour for the function a in the code, a combination of the sin and cos functions:
![Pi sticks example](/output/pi_sticks/20x20/black_Oranges_r_Blues.png)
