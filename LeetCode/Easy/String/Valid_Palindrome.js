/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const eng = /[a-z]/;
  const num = /[0-9]/;
  let word = "";
  const lower = s.toLowerCase().replace(/ /g, "");
  if (lower.length === 0) return true;
  for (var i = 0; i < lower.length; i++) {
    if (eng.test(lower[i]) || num.test(lower[i])) {
      word += lower[i];
    }
  }
  if (word.length === 0 || word.length === 1) return true;
  return isPalindrome(word);

  function isPalindrome(str) {
    const halfLength = parseInt(str.length / 2);
    for (var j = 0; j < halfLength; j++) {
      if (str[j] !== str[str.length - 1 - j]) {
        return false;
      }
    }
    return true;
  }
};
