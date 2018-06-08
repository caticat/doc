#include <iostream>
#include <string>
#include <execinfo.h>
#include <thread>
#include <signal.h>

using namespace std;

bool flag = true;

void test()
{
	while (flag)
	{
		cout << 1 << endl;
		this_thread::sleep_for(chrono::seconds(1));
	}
}

void SignalHandler(int sig)
{
	// 还原信号的处理方式
	signal(sig, SIG_DFL);

	// 输出下堆栈
	const int maxFrames = 100;
	void* frames[maxFrames];
	string result;
	int numFrames = backtrace(frames, maxFrames);
	char** symbols = backtrace_symbols(frames, numFrames);
	for (int i = 0; i < numFrames; i++)
	{
		cout << frames[i] << ":" << symbols[i] << endl;
	}

	// 停止运行
	flag = false;
}

void RegistSignalHandler()
{
	// 注册监听的信号handler函数
	signal(SIGINT, SignalHandler);
}

int main()
{
	cout << "开始" << endl;

	RegistSignalHandler();

	thread td(&test);

	td.join();

	cout << "结束" << endl;

	return 0;
}

