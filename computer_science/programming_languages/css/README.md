# Cascading Style sheets

## Spacing

### Padding

An element's `padding` controls the amount of space between the element's content and its `border`.

### Margin

An element's `margin` controls the amount of space between an element's `border` and surrounding elements.

---

- for specifying elements `padding-top`, `padding-right`, `padding-bottom`, `padding-left` use clockwise notation.
  this is applicable for `margin` also for `margin-top`, `margin-right`, `margin-bottom`, `margin-left`.

- The two main types of length units are absolute and relative.
- Absolute are `px`, `in`, `mm`.
- Relative are relative to parent, `em`, `rem`
- Sometimes your HTML elements will receive multiple styles that conflict with one another. if style applied by class selector, the class selector will override <body> element style selector.
- The second declaration will always take precedence over the first. look at the declaration order and not the order of their use!
- id selector takes precendence over class selector.
- inline CSS takes precendence over id selector;
- `!important` overrides all over selectors and takes precedence.
- CSS hexcode colors uses 6 hexadecimal places, 2 each for Red(R), Green(G) and Blue(B) pure colors, we can vary the amounts of each to create over 16 million other colors.
- 0 represents complete absence of color.
- Abbreviated Hex Code red's hex code `#FF0000` can be shortened to `#F00`. The shortened form has one digit each for Red, Green and Blue.
- Another way to use color as rgb() function values, 0 to 255 => 256 values which are same as 16 X 16 two hexadecimal places.
- CSS Variables are a powerful way to change many CSS style properties at once by changing only one value. it follows `--` double hyphen symbol to represent and declare, for usage of value, use `var(--variable, fallbackvalue)`.
- It's important to provide browser fallbacks to avoid potential problems. so create the property just above the usage like `variable` way.
- `:root` is a pseudo-class selector that matches the root element of the document, usually the `html` element. By creating your variables in `:root`, they will be available globally and can be accessed from any other selector in the style sheet.
- we can redefine the variable in the child classes, to override a variable definition.
- Use a media query to change a variable, For instance, when your screen is smaller or larger than your media query break point, you can change the value of a variable, and it will apply its style wherever it is used.

### text-align

`text-align: justify;` causes all lines of text except the last line to meet the left and right edges of the line box.

`text-align: center;` centers the text

`text-align: right;` right-aligns the text

And `text-align: left;` (the default) left-aligns the text.

### width

can be given in absolute or relative length units

`width: 20px;`

### height

same as width.
`height: 30px;`

### strong tag

same as `font-weight: bold`.
`<strong></strong>`

### u tag

for underline, same as `text-decoration: underline;`

`<u></u>`

### emphasize <em></em> tag, italic

`font-style: italic;`

`<em></em>`

### strike through <s></s> tag

```css
text-decoration: line-through;
```

```css
<s></s>
```

### horizantal line <hr> tag

`hr` tag to add a horizontal line across the width of its containing element.
`hr` is self closing tag.

### background-color

Instead of adjusting your overall background or the color of the text to make the foreground easily readable, you can add a `background-color` to the element holding the text you want to emphasize. This challenge uses `rgba()` instead of hex codes or normal rgb().
`a` in rgba() stands for = alpha/level of opacity.
The alpha value can range from `1`, which is fully opaque or a solid color, to `0`, which is fully transparent or clear.

Note: `background` is the supercede of

`background-color background-image background-position background-repeat background-attachment background-clip background-origin background-size`

### font-size

The `font-size` property is used to specify how large the text is in a given element, containing text.

### font-weight

The `font-weight` property sets how thick or thin characters are in a section of text.

### line-height

`line-height` property to change the height of each line in a block of text. As the name suggests, it changes the amount of vertical space that each line of text gets.

### box-shadow

The `box-shadow` property applies one or more shadows to an element.

The `box-shadow` property takes values for

`offset-x` (how far to push the shadow horizontally from the element),
`offset-y` (how far to push the shadow vertically from the element),
`blur-radius`,
`spread-radius` and
`color`, in that order.
The `blur-radius` and `spread-radius` values are optional.

Multiple box-shadows can be created by using commas to separate properties of each `box-shadow` element.

```css
box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
```

### opacity

The `opacity` property in CSS is used to adjust the opacity, or conversely, the transparency for an item.

- A value of 1 is opaque, which isn't transparent at all.
- A value of 0.5 is half see-through.
- A value of 0 is completely transparent.

`opacity: 0.7;`

### text-transform

ex: `text-transform: lowercase;`

| Value        | Result                                               |
| ------------ | ---------------------------------------------------- |
| `lowercase`  | "transform me"                                       |
| `uppercase`  | "TRANSFORM ME"                                       |
| `capitalize` | "Transform Me"                                       |
| `initial`    | Use the default value                                |
| `inherit`    | Use the text-transform value from the parent element |
| `none`       | Default: Use the original text                       |

### Pseudo classes

A pseudo-class is a keyword that can be added to selectors, in order to select a specific state of the element.
Lets say an anchor tag hover state needs to styled with color blue.

```css
/* normally it is black */
a {
  color: #000;
}
/* using pseudo classes we can set hover state of anchor tag having color blue. */
a:hover {
  color: blue;
}
```

### Relative position

CSS treats each HTML element as its own box, which is usually referred to as the `CSS Box Model`. `Block-level` items automatically start on a new line (think headings, paragraphs, and divs) while `inline items` sit within surrounding content (like images or spans). The default layout of elements in this way is called the `normal flow` of a document, but CSS offers the `position` property to override it.

When the `position` of an element is set to `relative`, it allows you to specify how CSS `should move it relative to its current position in the normal flow` of the page. It pairs with the CSS `offset` properties of `left` or `right`, and `top` or `bottom`. These say how many pixels, percentages, or ems to move the item away from where it is normally positioned. The following example moves the paragraph 10 pixels away from the bottom:

```css
p {
  position: relative;
  bottom: 10px;
}
```

Changing an element's position to relative `does not` remove it from the normal flow - other elements around it still behave as if that item were in its default position. Note: Positioning gives you a lot of flexibility and power over the visual layout of a page. It's good to remember that `no matter the position of elements`, the underlying `HTML markup` should be organized and make sense when `read from top to bottom`. This is how users with visual impairments (who rely on assistive devices like screen readers) access your content.

let's say if we move the paragraph `p` bottom by `200px` it will move the content down to page, where as the HTML markup will treat as it is on top and the assistive devices will read it as if it is on top.

![Relative position](./static/relative_position.gif)

Note: Using the top offset moved the HTML element downwards. Likewise, using a left offset moves an item to the right.

### Absolute Position

The next option for the CSS `position` property is `absolute`, which locks the element in place relative to its parent container. Unlike the relative position, this removes the element from the normal flow of the document, so surrounding items ignore it. Offset positions are same as relative position.

One nuance with absolute positioning is that it will be locked relative to its closest positioned ancestor. If you forget to add a position rule to the parent item, (this is typically done using `position: relative;`), the browser will keep looking up the chain and ultimately default to the `body` tag.

### Fixed position: Lock an Element to the Browser Window with Fixed Positioning

The next layout scheme that CSS offers is the `fixed` position, which is a type of `absolute` positioning that locks an element relative to the `browser window`. Similar to `absolute` positioning, it's used with the CSS offset properties and also removes the element from the normal flow of the document. Other items no longer `"realize"` where it is positioned, which may require some layout adjustments elsewhere.

One key difference between the `fixed` and `absolute` positions is that an element with a `fixed` position won't move when the user scrolls.

### Float property: Push Elements Left or Right with the float Property

The next positioning tool does not actually use position, but sets the `float` property of an element. Floating elements are removed from the normal flow of a document and pushed to either the `left` or `right` of their containing parent element. It's commonly used with the `width` property to specify how much horizontal space the floated element requires.

### Change the Position of Overlapping Elements with the z-index Property

z-index as think as Z axis in coordinate system.
When elements are positioned to `overlap` (i.e. using `position`: `absolute` | `relative` | `fixed` | `sticky`), the element coming later in the HTML markup will, by default, appear on the top of the other elements. However, the `z-index` property can specify the order of how elements are `stacked on top of one another`. It must be an integer (i.e. a whole number and not a decimal), and higher values for the z-index property of an element move it higher in the stack than those with lower values.

### Center an Element Horizontally Using the margin Property

Another positioning technique is to center a block element horizontally. One way to do this is to set its `margin` to a value of auto.

This method works for images, too. Images are `inline elements` by default, but can be changed to `block elements` when you set the `display` property to `block`.

### Learn about Complementary Colors

Color theory and its impact on design is a deep topic and only the basics are covered in the following challenges. On a website, color can draw attention to content, evoke emotions, or create `visual harmony`. Using different combinations of colors can really change the look of a website, and `a lot of thought` can go into picking a color palette that works with your content.

The `color wheel` is a useful tool to visualize how colors relate to each other - it's a circle where similar hues are neighbors and different hues are farther apart. When two colors are opposite each other on the wheel, they are called `complementary colors`. They have the characteristic that if they are combined, they "cancel" each other out and create a `gray color`. However, when placed `side-by-side`, these `colors appear more vibrant` and produce a strong visual contrast.

Some examples of complementary colors with their hex codes are:

```
red (#FF0000) and cyan (#00FFFF)
green (#00FF00) and magenta (#FF00FF)
blue (#0000FF) and yellow (#FFFF00)
```

This is different than the outdated RYB color model that many of us were taught in school, which has different primary and complementary colors. Modern color theory uses the additive `RGB` model (like on a computer screen) and the subtractive CMY(K) model (like in printing). Read [here](https://en.wikipedia.org/wiki/Color_model) for more information on this complex subject.

There are many color picking tools available online that have an option to find the complement of a color.

Note: For all color challenges: Using color can be a powerful way to add visual interest to a page. However, color alone should not be used as the only way to convey important information because users with visual impairments may not understand that content. This issue will be covered in more detail in the Applied Accessibility challenges.

### Learn about Tertiary Colors

Computer monitors and device screens create different colors by combining amounts of red, green, and blue light. This is known as the `RGB additive color model` in modern color theory. Red (R), green (G), and blue (B) are called primary colors. Mixing two primary colors creates the `secondary colors` cyan (G + B), magenta (R + B) and yellow (R + G). You saw these colors in the `Complementary Colors` challenge. These `secondary colors` happen to be the `complement` to the `primary color` not used in their creation, and are opposite to that primary color on the color wheel. For example, magenta is made with red and blue, and is the complement to green.

`Tertiary colors` are the result of combining a primary color with one of its `secondary color` neighbors. For example, within the RGB color model, red (`primary`) and yellow (`secondary`) make orange (`tertiary`). This adds six more colors to a simple color wheel for a total of twelve.

There are various methods of selecting different colors that result in a harmonious combination in design. One example that can use `tertiary colors` is called the `split-complementary` color scheme. This scheme starts with a `base color`, then pairs it with the two colors that are adjacent to its complement. The three colors provide strong visual contrast in a design, but are more subtle than using two complementary colors.

### Adjust the Color of Various Elements to Complementary Colors

The Complementary Colors challenge showed that opposite colors on the color wheel can make each other appear more vibrant when placed side-by-side. However, the strong visual contrast can be jarring if it's overused on a website, and can sometimes make text harder to read if it's placed on a complementary-colored background. In practice, one of the colors is usually dominant and the complement is used to bring visual attention to certain content on the page.

### Adjusting Hue of a color

Colors have several characteristics including `hue`, `saturation`, and `lightness`. CSS3 introduced the `hsl()` property as an alternative way to pick a color by directly stating these characteristics.

#### Hue

Hue is what people generally think of as 'color'. If you picture a `spectrum` of colors starting with `red` on the left, moving through `green` in the middle, and `blue` on right, the hue is where a color fits along this `line`. In `hsl()`, hue uses a `color wheel` concept instead of the spectrum, where the `angle` of the color on the `circle` is given as a value between 0 and 360.

#### Saturation

Saturation is the amount of `gray` in a color. A `fully saturated` color has `no gray` in it, and a `minimally saturated` color is almost `completely gray`. This is given as a `percentage` with 100% being fully saturated.

#### Lightness

Lightness is the amount of white or black in a color. A percentage is given ranging from `0% (black)` to `100% (white)`, where `50%` is the `normal color`.

Here are a few examples of using `hsl()` with `fully-saturated`, `normal lightness` colors:

| Color   | HSL                 |
| ------- | ------------------- |
| red     | hsl(0, 100%, 50%)   |
| yellow  | hsl(60, 100%, 50%)  |
| green   | hsl(120, 100%, 50%) |
| cyan    | hsl(180, 100%, 50%) |
| blue    | hsl(240, 100%, 50%) |
| magenta | hsl(300, 100%, 50%) |

### Adjust tone of color

The `hsl()` option in CSS also makes it easy to adjust the `tone` of a color. Mixing `white` with a `pure hue` creates a `tint` of that color, and `adding black` will make a `shade`. Alternatively, a `tone` is produced by adding `gray` or by both tinting and shading. Recall that the `'s'` and `'l'` of hsl() stand for `saturation` and `lightness`, respectively. The `saturation` percent `changes` the `amount of gray` and the `lightness` percent `determines how much white or black` is in the color. This is useful when you have a `base hue` you like, but need different variations of it.

### Other info

- The font size of header tags (h1 through h6) should generally be larger than the font size of paragraph tags
