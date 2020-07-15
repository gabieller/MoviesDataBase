sns.set_style("white")
ax = sns.scatterplot(x=base['Budget'], y=base['Revenue'])  
ax.set_yscale('log')
ax.set_xscale('log')

X_train, X_test, y_train, y_test = train_test_split(base.Budget, base.Revenue)

plt.scatter(X_train,y_train, label = "Training Data", color = "r", alpha= .7)
plt.scatter(X_test,y_test, label = "Testing Data", color = "g", alpha= .7)
plt.legend()
plt.yscale('log')
plt.xscale('log')


lr = LinearRegression()
lr.fit(X_train.values.reshape(-1,1), y_train.values)

prediction = lr.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label = "Linear Regression", color = "b")
plt.scatter(X_test,y_test, label = "Actual Test Data", color = "g", alpha=.7)
plt.legend()
plt.yscale('log')
plt.xscale('log')

sns.distplot(base['Budget'])

corre = np.corrcoef(base["Budget"],base["Revenue"])
