#pragma once
#include<type_traits>
#include<utility>

template<typename Callable>
union LambdaFunctionStorage
{
	LambdaFunctionStorage() {}
	std::decay_t<Callable> callable;
};

template<typename Callable, typename Ret, typename... Args>
auto LambdaFunctionPointer_(Callable&& c, Ret(*)(Args...))
{
	static bool used = false;
	static LambdaFunctionStorage<Callable> s;
	using type = decltype(s.callable);

	if (used)
		s.callable.~type();
	new (&s.callable) type(std::forward<Callable>(c));
	used = true;

	return [](Args... args) -> Ret {
		return Ret(s.callable(std::forward<Args>(args)...));
	};
}

template<typename Fn, typename Callable>
Fn* LambdaFunctionPointer(Callable&& c)
{
	return LambdaFunctionPointer_(std::forward<Callable>(c), (Fn*)nullptr);
}

// illustration:
//void test() {
//	int value = 42;
//	auto fn = LambdaFunctionPointer<void(int)>([&](int i) { ++value; std::cout << value << " / " << i; });
//	foo(fn, 123);  // compiles!
//	void (*tfn)(int) = fn;
//}
