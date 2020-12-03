/* $File: longest_increasing_subsequence.cc, $Timestamp: Thu Dec  3 17:47:03 2020 */
#ifdef LOCAL
#  include <algorithm>
#  include <assert.h>
#  include <bitset>
#  include <chrono>
#  include <complex>
#  include <deque>
#  include <functional>
#  include <iomanip>
#  include <iostream>
#  include <iterator>
#  include <limits>
#  include <list>
#  include <map>
#  include <math.h>
#  include <numeric>
#  include <queue>
#  include <random>
#  include <set>
#  include <sstream>
#  include <stack>
#  include <stdio.h>
#  include <stdlib.h>
#  include <string.h>
#  include <string>
#  include <time.h>
#  include <utility>
#  include <vector>
#else
#  include <bits/stdc++.h>
#endif

using namespace std;

/* All Required 'define' Pre-Processors and 'typedef' Constants. */
#define FOR(i, j, k, inc) for (ll i = j; i < k; i += inc)
#define RFOR(i, j, k, dec) for (ll i = j; i >= k; i -= dec)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define ALL(cont) begin(cont), end(cont)
#define RALL(cont) end(cont), begin(cont)
#define FOREACH(it, cont) for (auto it = begin(cont); it != end(cont); it++)
#define TRAV(e, cont) for (auto& e: cont)
#define pb push_back
#define mp make_pair
#define fst first
#define scd second
#define mv move
#define fwd forward
#define ASSERT(expr...) assert((expr))
#define IN(x, y, z) (y <= x && x <= z)
#define X_T_X template<typename T>
#define X_S_X template<size_t S>
#define X_T_S_X template<typename T, size_t S>
#define X_T_U_X template<typename T, typename U>
#define X_T_Us_X template<typename T, typename... Us>

/* Type Aliases. */
using ll = long long;
using ld = long double;
using db = double;
using str = string;
X_S_X using bits = bitset<S>;
X_T_S_X using arr = array<T, S>;
X_T_X using vec = vector<T>;
X_T_X using vvec = vector<vector<T>>;
X_T_X using vvvec = vector<vector<vector<T>>>;
X_T_X using cop = complex<T>;
X_T_X using pque = priority_queue<T, vector<T>>;
X_T_X using pquel = priority_queue<T, vector<T>, less<T>>;
X_T_X using pqueg = priority_queue<T, vector<T>, greater<T>>;

/* Constants. */
constexpr ll INF = 1010000000000000017LL;
constexpr ll MOD = 1000000007LL;
constexpr db EPS = 1e-12;
constexpr db PI = 3.14159265358979323846;
const mt19937 RNG((uint32_t)chrono::steady_clock::now().time_since_epoch().count());

/* Initialization Settings. */
struct INIT {
  static constexpr int IOS_PREC = 15;
  static constexpr bool AUTO_FLUSH = false;
  INIT() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(IOS_PREC);
    if (AUTO_FLUSH) cout << unitbuf;
  }
} INIT;
struct STDIN {
 public:
  STDIN(const string& path) { fd_ = freopen(path.c_str(), "r", stdin); }
  ~STDIN() { if (fd_) fclose(stdin); }
  operator bool(void) { return fd_ != nullptr; }
 private:
  FILE* fd_;
};
struct STDOUT {
 public:
  STDOUT(const string& path) { fd_ = freopen(path.c_str(), "w", stdout); }
  ~STDOUT() { if (fd_) fclose(stdout); }
  operator bool(void) { return fd_ != nullptr; }
 private:
  FILE* fd_;
};

/* Helper Functions. */
inline constexpr ll PCNT(const ll& x) { return static_cast<ll>(__builtin_popcountll(x)); }
inline constexpr ll BITS(const ll& x) { return static_cast<ll>(31 - __builtin_clzll(x)); }
inline ll CDIV(const ll& x, const ll& y) { return x / y + ((x ^ y) > 0 && x % y); }
inline ll FDIV(const ll& x, const ll& y) { return x / y - ((x ^ y) < 0 && x % y); }
X_T_X inline bool AMIN(T& x, const T& y) { return y < x ? x = y, 1 : 0; }
X_T_X inline bool AMAX(T& x, const T& y) { return x < y ? x = y, 1 : 0; }
X_T_X inline ll SIZE(const T& t) { return static_cast<ll>(t.size()); }
X_T_S_X inline ll SIZE(const T (&t)[S]) { return static_cast<ll>(S); }
X_T_Us_X inline void RESIZE(vector<T>& v, size_t&& s) { v.resize(s); }
X_T_Us_X inline void RESIZE(vector<T>& v, size_t&& s, Us&&... ss) { v.resize(s); TRAV (e, v) RESIZE(e, fwd<Us>(ss)...); }
X_T_U_X T FST(T l, T r, U p) { r++; ASSERT(l <= r); while (l < r) { T m = l + (r - l) / 2; p(m) ? r = m : l = m + 1; } return l; }
X_T_U_X T LST(T l, T r, U p) { l--; ASSERT(l <= r); while (l < r) { T m = l + (r - l + 1) / 2; p(m) ? l = m : r = m - 1; } return l; }
X_T_X void REMDUP(vec<T>& v) { sort(ALL(v)); v.erase(unique(ALL(v)), end(v)); }
X_T_U_X void ERASE(T& t, const U& u) { auto it = t.find(u); ASSERT(it != end(t)); t.erase(it); }

/* IO Functions. */
X_T_X void CIN(cop<T>& c);
X_T_U_X void CIN(pair<T, U>& p);
X_T_X void CIN(vec<T>& v);
X_T_S_X void CIN(arr<T, S>& a);
X_T_X inline void CIN(T& t) { cin >> t; }
inline void CIN(db& d) { str t; CIN(t); d = stod(t); }
inline void CIN(ld& d) { str t; CIN(t); d = stold(t); }
X_T_Us_X void CIN(T& t, Us&... us) { CIN(t); CIN(us...); }
X_T_X void CIN(cop<T>& c) { T a, b; CIN(a, b); c = {a, b}; }
X_T_U_X void CIN(pair<T, U>& p) { CIN(p.fst, p.scd); }
X_T_X void CIN(vec<T>& v) { TRAV(e, v) CIN(e); }
X_T_S_X void CIN(arr<T, S>& a) { TRAV(e, a) CIN(e); }
X_T_X void CINV(ll& n, vec<T>& v) { v.resize(n); TRAV(e, v) CIN(e); }
#define STR to_string
str STR(char c) { return str(1, c); }
str STR(const char* cs) { return static_cast<str>(cs); }
str STR(const str& s) { return s; }
str STR(const bool& b) { return STR(static_cast<ll>(b)); }
X_T_X str STR(const cop<T>& c) { ostringstream ss; ss << c; return ss.str(); }
X_S_X str STR(const bits<S>& bs) { str s = ""; REP (i, S) s += char('0' + bs[i]); return s; }
X_T_U_X str STR(const pair<T, U>& p);
X_T_X str STR(const T& cont) { str s = ""; FOREACH(it, cont)  s += STR(*it) + (next(it) != end(cont) ? " " : ""); return s; }
X_T_U_X str STR(const pair<T, U>& p) { return STR(p.fst) + " " + STR(p.scd); }
void ENDL() { cout << endl; }
void COUT() {}
X_T_Us_X void COUT(const T& t, Us&&... us) { cout << STR(t); cout << (sizeof...(us) ? " " : ""); COUT(fwd<Us>(us)...); }
void DEBUG() {}
X_T_Us_X void DEBUG(const T& t, Us&&... us) { cerr << STR(t); cerr << (sizeof...(us)  ? ", " : ""); DEBUG(fwd<Us>(us)...); }
#ifdef LOCAL
#  define DBG(...) do { cerr << #__VA_ARGS__ << ": "; DEBUG(__VA_ARGS__); cerr << " : at line: " << __LINE__ << endl; } while (0)
#else
#  define DBG(...)
#endif

/* Main Function.
 * Stuff you should look for:
 *  - int overflow, array bounds
 *  - special cases (n=1?)
 *  - do smth instead of nothing and stay organized
 *  - WRITE STUFF DOWN
 *  - DON'T GET STUCK ON ONE APPROACH
 */
ll n;
vec<ll> a;
vec<ll> dp;

int main(int argc, char* argv[]) {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " <input file name>" << endl;
    return 1;
  }

  STDIN stdin(argv[1]);
  if (!stdin) {
    cerr << "File open error: " << argv[1] << endl;
    return 1;
  }

  CIN(n); ASSERT(IN(n, 1, 1e3));
  CINV(n, a); REP (i, n) ASSERT(IN(a[i], 1, 1e6));
  DBG(n, a);

  //  RESIZE(dp, n);
  //  RREP (i, n - 1) {
  //    ll j = i + 1; while (j < n && a[j] <= a[i]) j++;
  //    dp[i] = j < n ? dp[j] + 1 : 1;
  //  }
  //  REP (i, n) AMAX(dp[0], dp[i]);
  //  COUT(dp[0]); ENDL();

  RESIZE(dp, n);
  fill(ALL(dp), INF);
  REP (i, n) {
    auto l = FST(0LL, n, [&](const ll& j) { return dp[j] > a[i]; });
    if (l < n) dp[l] = a[i];
  }

  COUT(LST(0LL, n, [&](const ll& i) { return dp[i] < INF; }) + 1); ENDL();

  return 0;
}
