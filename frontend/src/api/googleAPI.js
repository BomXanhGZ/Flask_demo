const { VITE_CLIENT_ID, VITE_REDIRECT_URI, VITE_GOOGLE_AUTH_URL } = import.meta.env

export const googleLogin = () => {
  const url_builder = VITE_GOOGLE_AUTH_URL
    + "?client_id=" + VITE_CLIENT_ID
    + "&redirect_uri=" + VITE_REDIRECT_URI
    + "&response_type=code"
    + "&scope=openid%20email%20profile"

  window.location.href = url_builder
}
