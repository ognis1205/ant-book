/*
 * Note: This template uses some c++11 functions , so you have to compile it with c++11 flag.
 *       Example:-   $ g++ -std=c++11 foo.cc
 *
 * Author : Shingo OKAWA
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
#define MP make_pair
#define PB push_back
#define FOR(i, j, k, inc) for (i64 i = j; i < k; i += inc)
#define RFOR(i, j, k, dec) for (i64 i = j; i >= k; i -= dec)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define ALL(cont) cont.begin(), cont.end()
#define RALL(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
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
inline void AMin(const T* t, const U& u) {
  if (u < *t) *t = u;
}

template<typename T, typename U>
inline void AMax(const T* t, const U& u) {
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
 * StoX and XtoS Functions.
 */
inline string to_string(char c) {
  return "'" + string({c}) + "'";
}

inline string to_string(bool b) {
  return b ? "true" : "false";
}

inline string to_string(const string& s) {
  return '"' + s + '"';
}

inline string to_string(const char* cs) {
  string ret(cs);
  return to_string(ret);
}

template<size_t N>
inline string to_string(const bitset<N>& bs) {
  string ret = "";
  for (i64 i = 0; i < SizeOf(bs); ++i) {
    ret += bs[i] + '0';
  }
  return to_string(ret);
}

template<typename T>
inline string to_string(const T& t);

template<typename T, typename U>
inline string to_string(const pair<T, U>& p) {
  return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template<typename T>
inline string to_string(const T& t) {
  i64 start = 0, end = kInf;
  string ret = "[";
  auto cur = begin(t);
  advance(cur, min(start, SizeOf(t)));
  for(i64 i = min(start, SizeOf(t)), j = min(end, SizeOf(t) - 1); i <= j; ++i) {
    ret += to_string(*cur) + (i != j ? ", " : "");
    cur = next(cur);
  }
  return ret + "]";
}

template<i64 Index, typename... Ts>
struct PrintTuple {
  string operator()(const tuple<Ts...>& t) const {
    string ret = PrintTuple<Index - 1, Ts...>{}(t);
    ret += (Index ? ", " : "");
    return ret + to_string(get<Index>(t));
  }
};

template<typename... Ts>
struct PrintTuple<0, Ts...> {
  string operator()(const tuple<Ts...>& t) const {
    return to_string(get<0>(t));
  }
};

template<typename... Ts>
inline string to_string(const tuple<Ts...>& t) {
  const auto Size = tuple_size<tuple<Ts...>>::value;
  return "(" + PrintTuple<Size - 1, Ts...>{}(t) + ")";
}

template <typename T>
inline T from_string(const string& s) {
  T ret;
  stringstream ss(s);
  ss >> ret;
  return ret;
}

/*
 * Debugging Class Template.
 */
#ifdef LOCAL
void Debug() {}

template<typename Head, typename... Tails>
void Debug(Head h, Tails... ts) {
  const auto Size = sizeof...(Tails);
  cerr << to_string(h) << (Size  ? ", " : "");
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

inline void SetStdin(string s) {
  freopen(s.c_str(), "r", stdin);
}

inline void SetStdout(string s) {
  freopen(s.c_str(), "w", stdout);
}

/*
 * User-defined Functions and Variables.
 */
struct NoOp {
  template<typename T>
  constexpr auto operator()(T&& t) const noexcept -> decltype(forward<T>(t)) {
    return forward<T>(t);
  }
};

struct Trim {
  string operator()(const string& s, const string& whitespace=" \n\r\t\f\v") const {
    const auto from = s.find_first_not_of(whitespace);
    if (from == string::npos) return "";
    const auto to = s.find_last_not_of(whitespace);
    const auto length = to - from + 1;
    return s.substr(from, length);
  }
};

template<typename T, class Preprocess=NoOp>
void SplitAs(const string& line,
             char delimiter,
             vector<T>& result,
             Preprocess&& preprocess=Preprocess()) {
  stringstream ss(line);
  string token;
  while (getline(ss, token, delimiter)) {
    result.push_back(from_string<T>(preprocess(token)));
  }
}

template<typename Order>
struct NonStrict : public binary_function<typename Order::second_argument_type,
                                          typename Order::first_argument_type,
                                          bool> {
  NonStrict(Order o) : order(o) {}
  bool operator()(typename Order::second_argument_type lhs,
                  typename Order::first_argument_type rhs) const {
    return !order(rhs, lhs);
  }
private:
  Order order;
};

template<typename Order>
NonStrict<Order> ToNonStrict(Order o) {
  return NonStrict<Order>(o);
}

template<class RandomAccessIterator, class Predicate>
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

template<class RandomAccessIterator, class Order>
void Sort(RandomAccessIterator begin, RandomAccessIterator end, Order order) {
  if (begin < end) {
    typedef typename iterator_traits<RandomAccessIterator>::value_type ValueType;
    ValueType pivot = *(begin + (end - begin) / 2);
    RandomAccessIterator l = Partition(begin, end, [pivot, order](ValueType& v) { return order(v, pivot) ? true : false; });
    RandomAccessIterator r = Partition(l, end, [pivot, order](ValueType& v) { return ToNonStrict(order)(v, pivot) ? true : false; });
    Sort(begin, l, order);
    Sort(r, end, order);
  }
}

template<class RandomAccessIterator>
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
      kk.PB(k[i] + k[j]);
    }
  }
  Sort(kk.begin(), kk.end(), less<i64>());
  DBG(kk);

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
  cin >> n >> m;
  SplitAs<i64>([](){ string l; cin >> l; return l; }(), ',', k);

  ASSERT(IN(n, 1, 50));
  ASSERT(IN(m, 1, 1e8));
  ASSERT(n == SizeOf(k));
  FOREACH (it, k) ASSERT(IN(*it, 1, 1e8));
  DBG(n, m);
  DBG(k);

  Solve(n, m, k);

  return 0;
}
