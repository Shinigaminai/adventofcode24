#include <algorithm>
#include <cstddef>
#include <fstream>
#include <iostream>
#include <iterator>
#include <ostream>
#include <string>
#include <vector>

std::vector<std::vector<char>> read_input(std::string filename) {
  std::ifstream file(filename);
  std::string input_string;
  std::vector<std::vector<char>> input_collection;
  if (file.is_open()) {
    while (getline(file, input_string)) {
      // std::cout << input_string << std::endl;
      std::vector<char> line_vec(input_string.begin(), input_string.end());
      input_collection.push_back(line_vec);
    }
  }
  return input_collection;
}

int count_word(std::vector<std::string> *input, std::string word) {
  int count = 0;
  for (std::string line : *input) {
    std::string::size_type pos = 0;
    while ((pos = line.find(word, pos)) != std::string::npos) {
      ++count;
      pos += word.length();
    }
  }
  return count;
}

int count_word_vertical(std::vector<std::vector<char>> *input,
                        std::string word) {
  int count = 0;
  size_t rows = input->size();
  size_t columns = input->at(0).size();
  for (int column = 0; column < columns; ++column) {
    for (int row = 0; row < rows - word.length() + 1; ++row) {
      for (int k = 0; k < word.length(); ++k) {
        if (input->at(row + k).at(column) != word.at(k))
          break;
        if (k == word.length() - 1)
          ++count;
      }
    }
  }
  return count;
}

int count_word_horizontal(std::vector<std::vector<char>> *input,
                          std::string word) {
  int count = 0;
  size_t rows = input->size();
  size_t columns = input->at(0).size();
  for (int row = 0; row < rows; ++row) {
    for (int column = 0; column < columns - word.length() + 1; ++column) {
      for (int k = 0; k < word.length(); ++k) {
        if (input->at(row).at(column + k) != word.at(k))
          break;
        if (k == word.length() - 1)
          ++count;
      }
    }
  }
  return count;
}

int count_word_diagonal(std::vector<std::vector<char>> *input,
                        std::string word) {
  int count = 0;
  size_t rows = input->size();
  size_t columns = input->at(0).size();
  for (int row = 0; row < rows - word.length() + 1; ++row) {
    // search diagonally to the right
    for (int column = 0; column < columns - word.length() + 1; ++column) {
      for (int k = 0; k < word.length(); ++k) {
        if (input->at(row + k).at(column + k) != word.at(k))
          break;
        if (k == word.length() - 1) {
          ++count;
          // std::cout << "Found word at " << column << "x" << row << std::endl;
        }
      }
    }
    // search diagonally to the left
    for (int column = word.length() - 1; column < columns; ++column) {
      for (int k = 0; k < word.length(); ++k) {
        if (input->at(row + k).at(column - k) != word.at(k))
          break;
        if (k == word.length() - 1) {
          ++count;
          // std::cout << "Found word at " << column << "x" << row << std::endl;
        }
      }
    }
  }
  return count;
}

int count_X_MAS(std::vector<std::vector<char>> *input) {
  int count = 0;
  std::string word = "MAS";
  size_t rows = input->size();
  size_t columns = input->at(0).size();
  // search for stencil on every row and column
  for (int row = 0; row < rows - word.length() + 1; ++row) {               // y
    for (int column = 0; column < columns - word.length() + 1; ++column) { // x
      // compare stencil
      int from_left = 0;
      int from_right = 0;
      // MAS ->
      for (int k = 0; k < 3; ++k) {
        if (input->at(row + k).at(column + k) != word.at(k))
          break;
        if (k == word.length() - 1) {
          ++from_left;
        }
      }
      // MAS <-
      for (int k = 0; k < 3; ++k) {
        if (input->at(row + 2 - k).at(column + k) != word.at(k))
          break;
        if (k == word.length() - 1) {
          ++from_right;
        }
      }
      // SAM ->
      for (int k = 0; k < 3; ++k) {
        if (input->at(row + k).at(column + k) != word.at(2 - k))
          break;
        if (k == word.length() - 1) {
          ++from_left;
        }
      }
      // SAM <-
      for (int k = 0; k < 3; ++k) {
        if (input->at(row + 2 - k).at(column + k) != word.at(2 - k))
          break;
        if (k == word.length() - 1) {
          ++from_right;
        }
      }
      if (from_left && from_right) {
        ++count;
      }
    }
  }
  return count;
}

int main() {
  int count = 0;
  auto input = read_input("day4.input.txt");
  count += count_word_horizontal(&input, "XMAS");
  count += count_word_horizontal(&input, "SAMX");
  count += count_word_vertical(&input, "XMAS");
  count += count_word_vertical(&input, "SAMX");
  count += count_word_diagonal(&input, "XMAS");
  count += count_word_diagonal(&input, "SAMX");
  std::cout << count << std::endl;
  std::cout << count_X_MAS(&input) << std::endl;
  return 0;
}