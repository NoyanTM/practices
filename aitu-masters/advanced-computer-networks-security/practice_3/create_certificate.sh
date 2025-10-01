# Current UTC time
now=$(date -u +"%Y%m%d%H%M%S")

# Add 100 seconds
end=$(date -u -d "+100 seconds" +"%Y%m%d%H%M%S")

# Re-issue cert with precise validity
openssl x509 -in cert.pem -out cert-100s.pem -signkey key.pem \
  -startdate "${now}Z" -enddate "${end}Z"
