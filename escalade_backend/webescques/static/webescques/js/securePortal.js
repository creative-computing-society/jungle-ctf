const validate = function() {
    key = document.getElementById("key").value;
    split = 3;
    if (key.substring(0, split) == 'mag') {
      if (key.substring(split*9, split*10) == '_si') {
        if (key.substring(split*12, split*15) == 'l_end') {
          if (key.substring(split*10, split*11) == 'gh_') {
            if (key.substring(split*3, split*4) == 'wer') {
              if (key.substring(split*7, split*9) == 'an_its') {
                if (key.substring(split, split*3) == 'net_po') {
                  if (key.substring(split*11, split*12) == 'til') {
                    if (key.substring(split*6, split*7) == 'oce') {
                      if (key.substring(split*4, split*6) == '_warm_') {
                        return true;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    alert("Invalid key");
    return false;
}