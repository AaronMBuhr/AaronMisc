#pragma once

template <typename T>
class Singleton {
public:
protected:
	Singleton() {};
	Singleton(const Singleton&) {};
	Singleton& operator=(const Singleton&) {};
	static T& instance() {
		static T instance_;
		return instance_;
	}
};