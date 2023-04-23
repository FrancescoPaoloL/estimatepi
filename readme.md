# Approximating the value of π
The code is a Python implementation of the Monte Carlo method for approximating the value of π (pi).

    """
        m = nr points within a distance of 1 from origin
        n = total number of dots in 2x2 square

        m / n ~~ Area Circle / Area Square
        m / n ~~ (pi * 1^2) / 2 * 2 

        so

        pi ~~ 4 * (m / n)

        see: https://academo.org/demos/estimating-pi-monte-carlo/
    """

The function uses the "random" module in Python to generate "n" random points, each of which has an x-coordinate and a y-coordinate. These points are generated within a 2x2 square.

The function then checks whether each point generated falls inside a circle inscribed in the square. This circle has a radius of 1, and is proportional to the area of π. For each point that falls inside the circle, the function increments the variable "m" by 1.

After all the points have been generated and checked, the function calculates the ratio of the number of points that fall inside the circle to the total number of points generated. Finally, it uses this ratio to estimate the value of π using the formula pi = 4 * (m/n).

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
Just Python 3.6.9
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



