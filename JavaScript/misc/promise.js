const PENDING = Symbol('PENDING');

const FULFILLED = Symbol('FULFILLED');

const REJECTED = Symbol('REJECTED');

const exec = (f, onResolved, onRejected) => {
};

class MyPromise {
  constructor(f) {
    this.#state = PENDING;

    this.#value = null;

    this.#next = null;

    const fire = () => {
    };

    const fulfilled = (value) => {
    };

    const rejected = (error) => {
      this.#state = REJECTED;
      this.#value = error;
    };

    const reject = (error) => {
    };

    const resolve = (value) => {
    };

    exec(f, resolve, reject);
  }
}
