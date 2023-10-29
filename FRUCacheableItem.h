#pragma once

template <typename T>
class FRUCacheableItem {
public:
	virtual void loadByCacheId(T id) = 0;
	virtual size_t getHash() = 0;
	virtual void discardFromCache() = 0;
};