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

### Other info

- The font size of header tags (h1 through h6) should generally be larger than the font size of paragraph tags
