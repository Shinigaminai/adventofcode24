#include <fstream>
#include <iostream>
#include <regex>
#include <string>

using namespace std;

int findmul(string s) {
  int result = 0;
  regex words_regex("(mul\\()[0-9]{1,3},[0-9]{1,3}\\)");
  auto words_begin = sregex_iterator(s.begin(), s.end(), words_regex);
  auto words_end = sregex_iterator();

  std::cout << "Found " << std::distance(words_begin, words_end) << " words:\n";

  for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
    smatch match = *i;
    string match_str = match.str();
    int comma_pos = match_str.find(',');
    int number1 = stoi(match_str.substr(4, comma_pos - 4));
    int number2 =
        stoi(match_str.substr(comma_pos + 1, match_str.size() - comma_pos - 2));
    // cout << match_str << ":" << number1 << ',' << number2 << '\n';
    result += (number1 * number2);
  }
  return result;
}

int main() {
  ifstream file;
  file.open("day3.input.txt");
  int result = 0;
  string input_string;
  if (file.is_open()) {
    while (getline(file, input_string)) {
      result += findmul(input_string);
    }
    file.close();
  } else {
    cerr << "Unable to open file!" << endl;
  }
  cout << result << endl;
  return 0;
}
