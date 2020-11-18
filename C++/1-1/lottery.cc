/*
 * Note: This template uses some c++11 functions, so you have to compile it with c++11 flag.
 *       Example:-   $ g++ -std=c++11 foo.cc
 *
 * Copyright (c) 2020-present, Shingo OKAWA.
 * All rights reserved.
 */
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

/*
 * All Required 'define' Pre-Processors and 'typedef' Constants.
 */
#define STR(args...) #args
#define CAT(x, y) x ## y
#define MEMSET(x, y) memset(x, (y), sizeof(x))
#define FOR(i, j, k, inc) for (i64 i = j; i < k; i += inc)
#define RFOR(i, j, k, dec) for (i64 i = j; i >= k; i -= dec)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define ALL(cont) begin(cont), end(cont)
#define RALL(cont) end(cont), begin(cont)
#define FOREACH(it, cont) for (auto it = begin(cont); it != end(cont); it++)
#define ASSERT(expr...) assert((expr))
#define IN(x, y, z) (y <= x && x <= z)

using i8 = int8_t;
using u8 = uint8_t;
using i16 = int16_t;
using u16 = uint16_t;
using i32 = int32_t;
using u32 = uint32_t;
using i64 = int64_t;
using u64 = uint64_t;
using f32 = float;
using f64 = double;

constexpr i64 kInf = 1010000000000000017LL;
constexpr i64 kMod = 1000000007LL;
constexpr f64 kEps = 1e-12;
constexpr f64 kPi = 3.14159265358979323846;

/*
 * Initialization Settings.
 */
struct Init {
  static constexpr int kIosPrecision = 15;
  static constexpr bool kAutoFlush = false;
  Init() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(kIosPrecision);
    if (kAutoFlush) cout << unitbuf;
  }
} INIT;

/*
 * Templates of Some Basic Operations.
 */
template<typename T, typename U>
inline void AMin(T* t, const U& u) {
  if (u < *t) *t = u;
}

template<typename T, typename U>
inline void AMax(T* t, const U& u) {
  if (*t < u) *t = u;
}

template<typename T>
inline i64 SizeOf(const T& t) {
  return static_cast<i64>(t.size());
}

template<typename T, size_t N>
inline i64 SizeOf(const T (&t)[N]) {
  return static_cast<i64>(N);
}

/*
 * IO Helper Functions.
 */
struct Stdin {
 public:
  Stdin(const string& path) { fd_ = freopen(path.c_str(), "r", stdin); }
  ~Stdin() { if (fd_) fclose(stdin); }
  operator bool(void) { return fd_ != nullptr; }
 private:
  FILE* fd_;
};

struct Stdout {
 public:
  Stdout(const string& path) { fd_ = freopen(path.c_str(), "w", stdout); }
  ~Stdout() { if (fd_) fclose(stdout); }
  operator bool(void) { return fd_ != nullptr; }
 private:
  FILE* fd_;
};

//template<typename T>
//using Callback = void (*)(const i64&, T*);

template<typename T, typename Callback>
class SplitAsManip {
 public:
  SplitAsManip(char delim, Callback& callback) : delim_(delim), callback_(callback) {}
  istream& operator()(istream& is) {
    i64 pos=0;
    string dsv; is >> dsv; istringstream iss(dsv);
    for (string token; getline(iss, token, delim_);) {
      T t; istringstream parse(token); parse >> t;
      callback_(pos++, &t);
    }
    return is;
  }
 private:
  char delim_;
  Callback& callback_;
};

template<typename Callback>
class SplitAsManip<char, Callback> {
 public:
  SplitAsManip(Callback& callback) : callback_(callback) {}
  istream& operator()(istream& is) {
    string s; is >> s;
    for (i64 i = 0; i < s.size(); i++) callback_(i, &s[i]);
    return is;
  }
 private:
  Callback& callback_;
};

template<typename T, typename Callback, typename enable_if<!is_same<T, char>::value, nullptr_t>::type=nullptr>
SplitAsManip<T, Callback> SplitAs(char delim, Callback&& callback) {
  return SplitAsManip<T, Callback>(delim, callback);
}

template<typename T, typename Callback, typename enable_if<is_same<T, char>::value, nullptr_t>::type=nullptr>
SplitAsManip<T, Callback> SplitAs(Callback&& callback) {
  return SplitAsManip<T, Callback>(callback);
}

template<typename T, typename Callback>
istream& operator>>(istream& is, SplitAsManip<T, Callback>&& manip) {
  return manip(is);
}

struct has_begin_end_empty {
  template<typename T>
  static auto check(T&& t) -> decltype(t.begin(), t.end(), t.empty(), true_type {});
  template<typename T>
  static auto check(...) -> false_type;
};

template<typename T>
struct is_container : public decltype(has_begin_end_empty::check<T>(declval<T>())) {};

template<typename T, typename U>
ostream& operator<<(ostream& os, const pair<T, U>& p) noexcept;

template<typename... Ts>
ostream& operator<<(ostream& os, const tuple<Ts...>& t) noexcept;

template<typename C,
         typename enable_if<is_container<C>::value && !is_same<C, string>::value, nullptr_t>::type=nullptr>
ostream& operator<<(ostream& os, const C& cont) noexcept {
  os << "[";
  for (auto it = begin(cont); it != end(cont); it++) os << *it << (next(it) != end(cont) ? ", " : "");
  return os << "]";
}

template<typename T,
         size_t N,
         typename enable_if<!is_same<T, char>::value, nullptr_t>::type=nullptr>
ostream& operator<<(ostream& os, const T (&arr)[N]) noexcept {
  os << "[";
  for (auto it = begin(arr); it != end(arr); it++) os << *it << (next(it) != end(arr) ? ", " : "");
  return os << "]";
}

template<size_t Index=0, typename... Ts>
inline typename enable_if<Index == sizeof...(Ts), void>::type
CopyTuple(ostream& os, const tuple<Ts...>& t) noexcept {}

template<size_t Index=0, typename... Ts>
inline typename enable_if<Index < sizeof...(Ts), void>::type
CopyTuple(ostream& os, const tuple<Ts...>& t) noexcept {
  os << get<Index>(t) << (Index == sizeof...(Ts) - 1 ? "" : ", ");
  CopyTuple<Index + 1, Ts...>(os, t);
}

template<typename... Ts>
ostream& operator<<(ostream& os, const tuple<Ts...>& t) noexcept {
  const auto Size = tuple_size<tuple<Ts...>>::value;
  os << "(";
  CopyTuple(os, t);
  return os << ")";
}

template<typename T, typename U>
ostream& operator<<(ostream& os, const pair<T, U>& p) noexcept {
  return os << "(" << p.first << ", " << p.second << ")";
}

/*
 * Macros of Simple Debugging Operations.
 */
#ifdef LOCAL
void Debug() {}

template<typename Head, typename... Tail>
void Debug(Head h, Tail... ts) {
  const auto Size = sizeof...(Tail);
  cerr << h << (Size  ? ", " : "");
  Debug(ts...);
}
#  define VER(...) do {\
                     cerr << "GCC version is " << __GNUC__ << "." << __GNUC_MINOR__ << "." << __GNUC_PATCHLEVEL__ << endl;\
                     cerr << "C++ version is " << __cplusplus << endl;\
                   } while (0)
#  define DBG(...) cerr << "\u001b[36m[DEBUG]\u001b[0m\t" << #__VA_ARGS__ << ": "; Debug(__VA_ARGS__); cerr << endl;
#else
#  define VER(...)
#  define DBG(...)
#endif

/*
 * User-defined Functions and Variables.
 */
i64 n, m;
vector<i64> k;

template<typename Order>
struct NonStrictOp : public binary_function<typename Order::second_argument_type,
                                            typename Order::first_argument_type,
                                            bool> {
  NonStrictOp(Order o) : order_(o) {}
  bool operator()(typename Order::second_argument_type lhs,
                  typename Order::first_argument_type rhs) const {
    return !order_(rhs, lhs);
  }
 private:
  Order order_;
};

template<typename Order>
NonStrictOp<Order> NonStrict(Order o) {
  return NonStrictOp<Order>(o);
}

template<typename RandomAccessIterator, typename Predicate>
RandomAccessIterator Partition(RandomAccessIterator begin,
                               RandomAccessIterator end,
                               Predicate&& predicate) {
  RandomAccessIterator ret = begin;
  for (auto it = begin; it != end; it++) {
    if (predicate(*it)) {
      if (it != ret) iter_swap(it, ret);
      ret++;
    }
  }
  return ret;
}

template<typename RandomAccessIterator, typename Order>
void Sort(RandomAccessIterator begin, RandomAccessIterator end, Order order) {
  if (begin < end) {
    typedef typename iterator_traits<RandomAccessIterator>::value_type ValueType;
    ValueType pivot = *(begin + (end - begin) / 2);
    RandomAccessIterator l = Partition(begin, end, [pivot, order](ValueType& v) { return order(v, pivot) ? true : false; });
    RandomAccessIterator r = Partition(l, end, [pivot, order](ValueType& v) { return NonStrict(order)(v, pivot) ? true : false; });
    Sort(begin, l, order);
    Sort(r, end, order);
  }
}

template<typename RandomAccessIterator>
bool Search(RandomAccessIterator begin,
            RandomAccessIterator end,
            typename iterator_traits<RandomAccessIterator>::value_type t) {
  RandomAccessIterator m = begin + (end - begin) / 2;
  if (begin + 1 == end) {
    return *begin == t;
  } else if (*m < t) {
    return Search(m + 1, end, t);
  } else if (*m == t) {
    return true;
  } else {
    return Search(begin, m - 1, t);
  }
}

void Solve() {
  vector<i64> kk;
  FOR (i, 0, n, 1) {
    FOR (j, i, n, 1) {
      kk.push_back(k[i] + k[j]);
    }
  }
  Sort(kk.begin(), kk.end(), less<i64>());

  REP (i, n) {
    REP (j, n) {
      if (m < kk[i] + kk[j]) continue;
      if (Search(kk.begin(), kk.end(), m - kk[i] - kk[j])) {
        cout << "Yes" << endl;
        return;
      }
    }
  }
  cout << "No" << endl;
}

/*
 * Main Function.
 */
int main(int argc, char* argv[]) {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " <input file name>" << endl;
    return 1;
  }

  Stdin stdin(argv[1]);
  if (!stdin) {
    cerr << "File open error: " << argv[1] << endl;
    return 1;
  }

  cin >> n >> m >> SplitAs<i64>(',', [&](const i64& i, i64* v) { k.emplace_back(*v); });

  ASSERT(IN(n, 1, 50));
  ASSERT(IN(m, 1, 1e8));
  ASSERT(n == SizeOf(k));
  FOREACH (it, k) ASSERT(IN(*it, 1, 1e8));

  DBG(n, m, k);
  Solve();

  return 0;
}
