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
#define IN(x, y, z) y <= x && x <= z

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
 * IO Helper Functions.
 */
inline void SetStdin(const string& s) {
  freopen(s.c_str(), "r", stdin);
}

inline void SetStdout(const string& s) {
  freopen(s.c_str(), "w", stdout);
}

struct has_emplace_back {
  template<typename T>
  static auto check(T&& t) -> decltype(t.emplace_back(), true_type {});
  template<typename T>
  static auto check(...) -> false_type;
};

struct has_emplace {
  template<typename T>
  static auto check(T&& t) -> decltype(t.emplace(), true_type {});
  template<typename T>
  static auto check(...) -> false_type;
};

template<typename T>
struct is_sequential : public decltype(has_emplace_back::check<T>(declval<T>())) {};

template<typename T>
struct is_associative : public decltype(has_emplace::check<T>(declval<T>())) {};

template<typename C, typename... Args>
inline typename enable_if<is_sequential<C>::value, void>::type
Append(C& cont, Args&&... args) {
  cont.emplace_back(forward<Args>(args)...);
}

template<typename C, typename... Args>
inline typename enable_if<is_associative<C>::value, void>::type
Append(C& cont, Args&&... args) {
  cont.emplace(forward<Args>(args)...);
}

template<typename T, typename Container, typename Preprocess>
class SplitAsManip {
 public:
  SplitAsManip(Container& cont,
               char delim,
               Preprocess& prep) : cont_(cont), delim_(delim), prep_(prep) {}
  istream& operator()(istream& is) {
    string dsv, token;
    is >> dsv;
    stringstream ss(dsv);
    while (getline(ss, token, delim_)) {
      T t;
      stringstream ss(prep_(token));
      ss >> t;
      Append(cont_, t);
    }
    return is;
  }
 private:
  Container& cont_;
  char delim_;
  Preprocess& prep_;
};

template<typename Container, typename Preprocess>
class SplitAsManip<char, Container, Preprocess> {
 public:
  SplitAsManip(Container& cont,
               char delim,
               Preprocess& prep) : cont_(cont), prep_(prep) {}
  istream& operator()(istream& is) {
    string s;
    is >> s;
    for (i64 i = 0; i < s.size(); i++) {
      Append(cont_, s[i]);
	}
    return is;
  }
 private:
  Container& cont_;
  Preprocess& prep_;
};

struct Skip {
  template<typename T>
  constexpr auto operator()(T&& t) const noexcept -> decltype(forward<T>(t)) {
    return forward<T>(t);
  }
};

template<typename T, typename Container, typename Preprocess=Skip>
SplitAsManip<T, Container, Preprocess> SplitAs(Container& cont,
                                               char delim,
                                               Preprocess&& prep=Preprocess()) {
  return SplitAsManip<T, Container, Preprocess>(cont, delim, prep);
}

template<typename T, typename Container, typename Preprocess>
istream& operator>>(istream& is, SplitAsManip<T, Container, Preprocess>&& manip) {
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
         typename enable_if<is_container<C>::value && !is_same<C, string>::value && !is_same<C, wstring>::value,
                            nullptr_t>::type=nullptr>
ostream& operator<<(ostream& os, const C& cont) noexcept {
  os << "[";
  for (auto it = begin(cont); it != end(cont); it++) {
    os << *it << (next(it) != end(cont) ? ", " : "");
  }
  return os << "]";
}

template<typename T,
         size_t N,
         typename enable_if<!is_same<T, char>::value && !is_same<T, wchar_t>::value,
                            nullptr_t>::type=nullptr>
ostream& operator<<(ostream& os, const T (&arr)[N]) noexcept {
  os << "[";
  for (auto it = begin(arr); it != end(arr); it++) {
    os << *it << (next(it) != end(arr) ? ", " : "");
  }
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
                     cerr << "GCC version is " << __GNUC__ << "." << __GNUC_MINOR__ << "." << __GNUC_PATCHLEVEL__ << endl; \
                     cerr << "C++ version is " << __cplusplus << endl;\
                   } while (0)
#  define DBG(...) cerr << "[DEBUG]\t" << #__VA_ARGS__ << ": "; Debug(__VA_ARGS__); cerr << endl;
#else
#  define VER(...)
#  define DBG(...)
#endif

/*
 * User-defined Functions and Variables.
 */
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

void Solve(i64 n, i64 m, const vector<i64>& k) {
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
    return 0;
  }
  SetStdin(argv[1]);

  i64 n, m;
  vector<i64> k;
  cin >> n >> m >> SplitAs<i64>(k, ',');

  ASSERT(IN(n, 1, 50));
  ASSERT(IN(m, 1, 1e8));
  ASSERT(n == SizeOf(k));
  FOREACH (it, k) ASSERT(IN(*it, 1, 1e8));

  DBG(n, m, k);
  Solve(n, m, k);

  return 0;
}
