#matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB.
#Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area,
#decorates the plot with labels, etc. In matplotlib.pyplot various states are preserved across function calls,
#so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed
#to the current axes (please note that “axes” here and in most places in the documentation refers to the axes part of
# a figure and not the strict mathematical term for more than one axis).

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')

#why is x-axis numbered from 0 to 3?
# If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and
#automatically generates the x values for you.
#Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x data are [0,1,2,3].

#plot() is versatile, pass in x and y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

#The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. 
#The default format string is ‘b-‘, which is a solid blue line. For example, to plot the above with red circles, you would issue

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
#plt.show()


#See the plot() documentation for a complete list of line styles and format strings.
#The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.

#If matplotlib were limited to working with lists, it would be fairly useless for numeric processing.
#Generally, you will use numpy arrays. In fact, all sequences are converted to numpy arrays internally.
#The example below illustrates a plotting several lines with different format styles in one command using arrays.


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

#Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; see matplotlib.lines.Line2D.
#There are several ways to set line properties
# https://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D

plt.plot(x, y, linewidth=2.0)

#plot returns a list of Line2D objects; e.g., line1, line2 = plot(x1, y1, x2, y2).
#In the code below we will suppose that we have only one line so that the list returned is of length 1.
#We use tuple unpacking with line, to get the first element of that list:

line, = plt.plot(x, y, '-')
line.set_antialiased(False) # turn off antialising

#Working with multiple figures and axe
#MATLAB, and pyplot, have the concept of the current figure and the current axes. All plotting commands apply to the current axes.

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

#The figure() command here is optional because figure(1) will be created by default, just as a subplot(111) will be created by default if you don’t manually specify any axes.
#The subplot() command specifies numrows, numcols, fignum where fignum ranges from 1 to numrows*numcols. The commas in the subplot command are optional if numrows*numcols<10. So subplot(211) is identical to subplot(2, 1, 1).


plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

#You can clear the current figure with clf() and the current axes with cla(). 

#Working with text
#The text() command can be used to add text in an arbitrary location, and the xlabel(), ylabel() and title() are used to add text in the indicated locations (see Text introduction for a more detailed example)


# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)


#Customize text
t = plt.xlabel('my data', fontsize=14, color='red')


#tex in text
plt.title(r'$\sigma_i=15$')

#The r preceding the title string is important – it signifies that the string is a raw string and not to treat backslashes as python escapes

#Annotating text

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()

#In this basic example, both the xy (arrow tip) and xytext locations (text location) are in data coordinates. Can use pixels too

#Log plotting
# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)


#can add your own scale too

#Framework of matplotlib http://pbpython.com/images/matplotlib-anatomy.png
#Framework example http://pbpython.com/images/matplotlib-pbpython-example.png


#Scatter plots

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

plt.axes([0.025,0.025,0.95,0.95])
plt.scatter(X,Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5,1.5), plt.xticks([])
plt.ylim(-1.5,1.5), plt.yticks([])
# savefig('../figures/scatter_ex.png',dpi=48)
plt.show()

#Bar plot
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.axes([0.025,0.025,0.95,0.95])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

for x,y in zip(X,Y2):
    plt.text(x+0.4, -y-0.05, '%.2f' % y, ha='center', va= 'top')

plt.xlim(-.5,n), plt.xticks([])
plt.ylim(-1.25,+1.25), plt.yticks([])

# savefig('../figures/bar_ex.png', dpi=48)


#Contour
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.axes([0.025,0.025,0.95,0.95])

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=10)

plt.xticks([]), plt.yticks([])
# savefig('../figures/contour_ex.png',dpi=48)


#3d plots
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
ax.set_zlim(-2,2)

# savefig('../figures/plot3d_ex.png',dpi=48)


#Quick references
#https://www.labri.fr/perso/nrougier/teaching/matplotlib/#quick-references
#https://www.labri.fr/perso/nrougier/teaching/matplotlib/#figures-subplots-axes-and-ticks
