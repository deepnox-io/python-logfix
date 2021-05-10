LOG_STRING = """2021-05-04T00:36:30,062Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,192Z		[SimpleAsyncTaskExecutor-104]	ERREUR	c.s.s.l.p.w.c.PlatformTrackListenableFuture	BUSINESS	Fake error trace: 	
javax.websocket.DeploymentException: Handshake error.
	at org.glassfish.tyrus.client.ClientManager$3$1.run(ClientManager.java:658) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.client.ClientManager$3.run(ClientManager.java:696) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511) ~[?:1.8.0_292]
	at java.util.concurrent.FutureTask.run(FutureTask.java:266) [?:1.8.0_292]
	at org.glassfish.tyrus.client.ClientManager$SameThreadExecutorService.execute(ClientManager.java:849) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at java.util.concurrent.AbstractExecutorService.submit(AbstractExecutorService.java:112) ~[?:1.8.0_292]
	at org.glassfish.tyrus.client.ClientManager.connectToServer(ClientManager.java:493) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.client.ClientManager.connectToServer(ClientManager.java:337) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.springframework.web.socket.client.standard.StandardWebSocketClient.lambda$doHandshakeInternal$0(StandardWebSocketClient.java:150) ~[spring-websocket-5.1.8.RELEASE.jar!/:5.1.8.RELEASE]
	at java.util.concurrent.FutureTask.run(FutureTask.java:266) [?:1.8.0_292]
	at java.lang.Thread.run(Thread.java:748) [?:1.8.0_292]
Caused by: org.glassfish.tyrus.core.HandshakeException: Response code was not 101: 429.
	at org.glassfish.tyrus.client.TyrusClientEngine.processResponse(TyrusClientEngine.java:299) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.ClientFilter.processRead(ClientFilter.java:167) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.Filter.onRead(Filter.java:111) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.Filter.onRead(Filter.java:113) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.SslFilter.handleRead(SslFilter.java:383) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.SslFilter.processRead(SslFilter.java:345) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.Filter.onRead(Filter.java:111) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.Filter.onRead(Filter.java:113) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.TransportFilter$4.completed(TransportFilter.java:294) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at org.glassfish.tyrus.container.jdk.client.TransportFilter$4.completed(TransportFilter.java:278) ~[tyrus-standalone-client-jdk-1.17.jar!/:?]
	at sun.nio.ch.Invoker.invokeUnchecked(Invoker.java:126) ~[?:1.8.0_292]
	at sun.nio.ch.Invoker$2.run(Invoker.java:218) ~[?:1.8.0_292]
	at sun.nio.ch.AsynchronousChannelGroupImpl$1.run(AsynchronousChannelGroupImpl.java:112) ~[?:1.8.0_292]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) ~[?:1.8.0_292]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) ~[?:1.8.0_292]
	... 1 more
2021-05-04T00:36:30,062Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace.	
2021-05-04T00:36:30,162Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,262Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,362Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,462Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace
2021-05-04T00:36:30,562Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake error trace 	
java.lang.NullPointerException: Oops!
    at com.ericgoebelbecker.stacktraces.StackTrace.d(StackTrace.java:28)
    at com.ericgoebelbecker.stacktraces.StackTrace.c(StackTrace.java:24)
    at com.ericgoebelbecker.stacktraces.StackTrace.b(StackTrace.java:20)
    at com.ericgoebelbecker.stacktraces.StackTrace.a(StackTrace.java:16)
    at com.ericgoebelbecker.stacktraces.StackTrace.main(StackTrace.java:9)
2021-05-04T00:36:31,062Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace.	
2021-05-04T00:36:31,162Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:31,177Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake error trace	
c.s.s.l.p.w.ConnectionException: MSGE008
	at sun.reflect.GeneratedMethodAccessor426.invoke(Unknown Source) ~[?:?]
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) ~[?:1.8.0_282]
	at java.lang.reflect.Method.invoke(Method.java:498) ~[?:1.8.0_282]
	at org.springframework.aop.support.AopUtils.invokeJoinpointUsingReflection(AopUtils.java:343) ~[spring-aop-5.1.8.RELEASE.jar!/:5.1.8.RELEASE]
	at org.springframework.aop.framework.ReflectiveMethodInvocation.invokeJoinpoint(ReflectiveMethodInvocation.java:198) ~[spring-aop-5.1.8.RELEASE.jar!/:5.1.8.RELEASE]
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163) ~[spring-aop-5.1.8.RELEASE.jar!/:5.1.8.RELEASE]
	at org.springframework.aop.interceptor.AsyncExecutionInterceptor.lambda$invoke$0(AsyncExecutionInterceptor.java:115) ~[spring-aop-5.1.8.RELEASE.jar!/:5.1.8.RELEASE]
	at java.util.concurrent.ForkJoinTask$AdaptedCallable.exec(ForkJoinTask.java:1424) [?:1.8.0_282]
	at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289) [?:1.8.0_282]
	at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056) [?:1.8.0_282]
	at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692) [?:1.8.0_282]
	at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:175) [?:1.8.0_282]
2021-05-04T00:36:30,162Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,262Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,362Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
2021-05-04T00:36:30,462Z		[pool-8-thread-1]	INFO 	c.s.s.l.p.w.PlatformTrackWebSocketClient	BUSINESS	Fake business trace	
"""
