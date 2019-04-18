
### 本库只放一些主要代码,仅供参考。



### 语音格式

	其他语音格式请用ffmpeg转换成pcm格式的，否则会出现识别失败的情况。



### c++打包成so，运行的主要命令是

	[root@c3 asr]# make
	g++ -shared -o src/libasr.so  ./src/asr.cpp -I../../include -I../../include/ASR  -Wall -O0 -fPIC -g -D__LINUX__ -Wno-unknown-pragmas -D_GLIBCXX_USE_CXX11_ABI=0  -std=c++11 ../../lib/libBDSpeechSDK.a ../../extern/lib/libjsoncpp.a ../../extern/lib/libcurl.a ../../extern/lib/libiconv.a ../../extern/lib/libz.a ../../extern/lib/libssl.a ../../extern/lib/libcrypto.a ../../extern/lib/libuuid.a -lrt -ldl -lpthread 



### python3.7.x调用生成的libasr.so


三段语音识别结果:


	{"error":0,"list":[{"thread_id":0,"txt":"今天天气怎样？"},{"thread_id":1,"txt":"小熊是一个大傻逼。你听得懂吗？"},{"thread_id":2,"txt":"早餐巴比馒头七块五。"}]}