const PENDING = Symbol('PENDING');

const FULFILLED = Symbol('FULFILLED');

const REJECTED = Symbol('REJECTED');

const exec = (f, onFulfilled, onRejected) => {
  let done = false;
  try {
    f(
      (value) => {
        if (done) return;
        done = true;
        onFulfilled(value);
      },
      (error) => {
        if (done) return;
        done = true;
        onRejected(error);
      }
    );
  } catch(error) {
    if (done) return;
    done = true;
    onRejected(error);
  }
};

const maybeThen = (maybePromise) => {
  if (maybePromise instanceof MyPromise &&
      typeof maybePromise.then == 'function')
    return maybePromise.then;
  return null;
};

class MyPromise {
  constructor(f) {
    this.#state = PENDING;

    this.#value = null;

    this.#next = null;

    const next = () => {
      if (this.#state === FULFILLED &&
          this.#next &&
          typeof this.#next.onFulfilled === 'function')
        this.#next.onFulfilled(this.#value);
      if (this.#state === REJECTED &&
          this.#next &&
          typeof this.#next.onRejected === 'function')
        this.#next.onRejected(this.#value);
    };

    const fulfilled = (value) => {
      this.#state = FULFILLED;
      this.#value = error;
      next();
    };

    const rejected = (error) => {
      this.#state = REJECTED;
      this.#value = error;
      next();
    };

    const reject = (error) => {
      rejected(error);
    };

    const resolve = (value) => {
      try {
        const then = maybeThen(value);
        if (then) {
          exec(then.bind(value), resolve, reject);
          return;
        }
        fulfilled(value);
      } catch(error) {
        rejected(error);
      }
    };

    exec(f, resolve, reject);
  }
}
