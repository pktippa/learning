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
- Absolute are `in`, `mm`.
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
