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

template<typename T, typename FunctionObject>
class SplitAsManip {
 public:
  SplitAsManip(char delim, FunctionObject& func) : delim_(delim), func_(func) {}
  istream& operator()(istream& is) {
    i64 pos=0;
    string token;
    string dsv; is >> dsv; stringstream ss(dsv);
    while (getline(ss, token, delim_)) {
      T t; stringstream ss(token); ss >> t;
      func_(pos, t);
      pos++;
    }
    return is;
  }
 private:
  char delim_;
  FunctionObject& func_;
};

template<typename FunctionObject>
class SplitAsManip<char, FunctionObject> {
 public:
  SplitAsManip(char delim, FunctionObject& func) : func_(func) {}
  istream& operator()(istream& is) {
    string s; is >> s;
    for (i64 i = 0; i < s.size(); i++) func_(i, s[i]);
    return is;
  }
 private:
  FunctionObject& func_;
};

template<typename T,
         typename FunctionObject,
         typename enable_if<is_same<T, char>::value, nullptr_t>::type=nullptr>
SplitAsManip<T, FunctionObject> SplitAs(FunctionObject&& func) {
  return SplitAsManip<T, FunctionObject>('\0', func);
}

template<typename T,
         typename FunctionObject,
         typename enable_if<!is_same<T, char>::value, nullptr_t>::type=nullptr>
SplitAsManip<T, FunctionObject> SplitAs(char delim, FunctionObject&& func) {
  return SplitAsManip<T, FunctionObject>(delim, func);
}

template<typename T, typename FunctionObject>
istream& operator>>(istream& is, SplitAsManip<T, FunctionObject>&& manip) {
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
  for (auto it = begin(cont); it != end(cont); it++) {
    os << *it << (next(it) != end(cont) ? ", " : "");
  }
  return os << "]";
}

template<typename T,
         size_t N,
         typename enable_if<!is_same<T, char>::value, nullptr_t>::type=nullptr>
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
i64 N;
vector<i64> ss, ts;

void Solve() {
  return;
}

string& Clean(string* line) {
  line->erase(remove(line->begin(), line->end(), ' '), line->end());
  i64 nested=0;
  for (char& c : *line) {
    if (c == '{') nested++;
    if (c == '}') nested--;
    if (nested == 0 && c == ',') c = '/';
  }
  return *line;
}

void CsvToV(const string& s, vector<i64>* v) {
  string l;
  istringstream iss(s);
  while (getline(iss, l, ',')) {
    v->push_back(stoll(l));
  }
}

void Parse(const i64& i, string s) {
  i64 pos=0;
  string key;
  if ((pos = s.find("=")) != string::npos) {
    key = s.substr(0, pos);
    s.erase(0, pos + 1);
    s.erase(remove_if(s.begin(), s.end(), [](char c){ return c == '{' || c == '}'; }), s.end());
    if (key == "N") {
      N = stoll(s);
    } else if (key == "s") {
      CsvToV(s, &ss);
    } else if (key == "t") {
      CsvToV(s, &ts);
    }
  } else {
    throw exception();
  }
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

  string line;
  while (getline(cin, line)) {
    istringstream iss(Clean(&line));
    iss >> SplitAs<string>('/', Parse);
  }

  ASSERT(IN(N, 1, 1e5));
  FOREACH (it, ss) ASSERT(IN(*it, 0, 1e5));
  FOREACH (it, ts) ASSERT(IN(*it, 0, 1e5));

  DBG(N, ss, ts);
  Solve();
  return 0;
}
