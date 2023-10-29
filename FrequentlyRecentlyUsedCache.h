#pragma once

#include <memory>
#include <vector>

using namespace std;

template <typename T>
class FrequentlyRecentlyUsedCache {

private:
	unique_ptr<vector<size_t>> hit_weights_;

};