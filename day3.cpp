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

enum State { ACTIVE, INACTIVE };

int main() {
  ifstream file;
  file.open("day3.input.txt");
  int result = 0;
  State state = ACTIVE;
  string input_string;
  if (file.is_open()) {
    while (getline(file, input_string)) {
      // part 1
      // result += findmul(input_string);
      // part 2
      cout << "read new line" << endl;
      while (!input_string.empty()) {
        if (state == ACTIVE) {
          auto dont_pos = input_string.find("don't()");
          result += findmul(input_string.substr(0, dont_pos));
          cout << "Found don't() at pos " << dont_pos << endl;
          if (dont_pos == string::npos)
            break;
          input_string = input_string.substr(dont_pos + 7);
          state = INACTIVE;
        }
        auto do_pos = input_string.find("do()");
        cout << "Found do() at pos " << do_pos << endl;
        if (do_pos == string::npos)
          break;
        input_string = input_string.substr(do_pos + 4);
        state = ACTIVE;
      }
    }
    file.close();
  } else {
    cerr << "Unable to open file!" << endl;
  }
  cout << result << endl;
  return 0;
}
