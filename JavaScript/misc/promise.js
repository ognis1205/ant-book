const PENDING = Symbol('PENDING');

const FULFILLED = Symbol('FULFILLED');

const REJECTED = Symbol('REJECTED');

const exec = (f, resolve, reject) => {
  let isRejected = false;
  try {
    f(
      (value) =>
        resolve(value),
      (error) => {
        isRejected = true;
        reject(error);
      }
    );
  } catch(error) {
    if (isRejected) return;
    reject(error);
  }
};

const maybeThen = (maybePromise) => {
  if (maybePromise instanceof MyPromise)
    return maybePromise.then;
  return null;
};

class EventHandler {
  constructor(onFulfilled, onRejected) {
    this.onFulfilled = onFulfilled;
    this.onRejected = onRejected;
  }
}

class MyPromise {
  constructor(f) {
    this.state = PENDING;
    
    this.value = null;
    
    this.handler = null;
    
    const callback = () => {
      if (
        this.state === FULFILLED &&
        this.handler &&
        typeof this.handler.onFulfilled === 'function'
      ) {
        this.handler.onFulfilled(this.value);
      } else if (
        this.state === REJECTED &&
        this.handler &&
        typeof this.handler.onRejected === 'function') {
        this.handler.onRejected(this.value);
      }
    };

    const fulfill = (value) => {
      this.state = FULFILLED;
      this.value = value;
      callback();
    };

    const reject = (error) => {
      this.state = REJECTED;
      this.value = error;
      callback();
    };

    const resolve = (value) => {
      try {
        const then = maybeThen(value);
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

  addHandler = (onFulfilled, onRejected) => {
    setTimeout(() => {
      if (this.state === PENDING) {
        this.handler = new EventHandler(onFulfilled, onRejected);
      } else if (this.state === FULFILLED && typeof onFulfilled === 'function') {
        onFulfilled(this.value);
      } else if (this.state === REJECTED && typeof onRejected === 'function') {
        onRejected(this.value);
      }
    });
  };

  then = (onFulfilled, onRejected) => {
    return new MyPromise((resolve, reject) => {
      this.addHandler(
        (value) => {
          if (onFulfilled) {
            try {
              resolve(onFulfilled(value));
            } catch(error) {
              reject(error);
            }
          } else {
            resolve(value);
          }
        },
        (error) => {
          if (onRejected) {
            resolve(onRejected(error))
          } else {
            reject(error);
          }
        }
      );
    });
  };

  catch = (onRejected) => {
    return new MyPromise((resolve, reject) => {
      this.addHandler(
        (value) => {
          resolve(value);
        },
        (error) => {
          try {
            resolve(onRejected(error));
          } catch(error) {
            reject(error);
          }
        }
      );
    });
  };
}

const promise = new MyPromise((resolve, reject) => {
  setTimeout(() => {
    resolve('first one');
  });
});

promise
  .then((value) => {
    console.log(value);
    return new MyPromise((resolve, reject) => {
      resolve(value + ' and second one');
    });
  })
  .then((value) => {
    console.log(value);
    throw new Error('error occured');
  })
  .then(
    (value) => {
      console.log(value);
    })
  .catch(
    (error) => {
      console.log('error catched');
    }
  );
