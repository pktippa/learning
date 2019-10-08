class X {
  x: Number;
}

class Y extends X {

}

class Z extends X {

}

class A {
  a?: Number;
}

class B extends A {

}
type P = A | X;

const m: P = {

};

const l = <A>m.a;
// const p = <X>m.x;
