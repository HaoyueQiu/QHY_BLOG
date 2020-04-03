export default {
  state: {
    is_authenticated: false,
    username: '',
    authority: false,
  },
  loginAction(username) {
    console.log('loginAction is triggered');
    this.state.is_authenticated = true;
    this.state.username = username
  },
  logoutAction() {
    console.log('logoutAction is triggered');
    window.localStorage.removeItem('blog-token');
    this.state.is_authenticated = false;
    this.state.username = ''
  },
}
