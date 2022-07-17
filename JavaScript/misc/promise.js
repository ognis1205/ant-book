const PENDING = Symbol('PENDING');

const FULFILLED = Symbol('FULFILLED');

const REJECTED = Symbol('REJECTED');

const exec = (f, onFulfilled, onRejected) => {
  let errorIsHandled = false;
  try {
    f(
      (value) => {
        onFulfilled(value);
      },
      (error) => {
        errorIsHandled = true;
        onRejected(error);
      }
    );
  } catch(error) {
    if (errorIsHandled) return;
    onRejected(error);
  }
};

const Callbacks = (onFulfilled, onRejected) => ({
  onFulfilled: onFulfilled,
  onRejected: onRejected,
});

const maybeThen = (maybePromise) => {
  if (maybePromise instanceof MyPromise &&
      typeof maybePromise.then == 'function')
    return maybePromise.then;
  return null;
};

class MyPromise {
  constructor(f) {
    this.state = PENDING;

    this.value = null;

    this.callbacks = null;

    const next = () => {
      if (this.state === FULFILLED &&
          this.callbacks &&
          typeof this.callbacks.onFulfilled === 'function')
        this.callbacks.onFulfilled(this.value);
      if (this.state === REJECTED &&
          this.callbacks &&
          typeof this.callbacks.onRejected === 'function')
        this.callbacks.onRejected(this.value);
    };

    const fulfill = (value) => {
      this.state = FULFILLED;
      this.value = value;
      next();
    };

    const reject = (error) => {
      this.state = REJECTED;
      this.value = error;
      next();
    };

    const resolve = (value) => {
      const then = maybeThen(value);
      try {
        if (then)
          exec(then.bind(value), resolve, reject);
        else
          fulfill(value);
      } catch(error) {
        reject(error);
      }
    };

    exec(f, resolve, reject);
  }

  chain(callbacks) {
    const self = this;
    setTimeout(() => {
      if (self.state === PENDING)
        self.callbacks = callbacks;
      else if (self.state === FULFILLED &&
               typeof callbacks.onFulfilled === 'function')
        callbacks.onFulfilled(self.value);
      else if (self.state === REJECTED &&
               typeof callbacks.onRejected === 'function')
        callbacks.onRejected(self.value);
    });
  }

  then(onFulfilled, onRejected) {
    const self = this;
    return new MyPromise((resolve, reject) => {
      self.chain(Callbacks(
        (value) => {
          if (typeof onFulfilled === 'function')
            try {
              resolve(onFulfilled(value));
            } catch(error) {
              reject(error);
            }
          else
            resolve(value);
        },
        (error) => {
          if (typeof onRejected === 'function')
            resolve(onRejected(error));
          else
            reject(error);
        }
      ));
    });
  }
}

promise = new MyPromise((resolve, reject) => {
  setTimeout(() => resolve('resolved first one'), 1000);
});

promise
  .then((res) => {
    console.log(res);
    return new MyPromise((resolve, reject) => {
      setTimeout(() => resolve('resolved second one after ' + res), 1000);
    });
  })
  .then(res => {
    console.log(res);
  });
