import { Injectable } from '@nestjs/common';

// このデコレータでproviderとして認識される。
// controllerのconstructorからDIされる。
@Injectable()
export class AppService {
  // controllerと同じメソッド名がわかりやすい (が同じでなくても良い)
  getHello(): string {
    return 'Hello World!';
  }
}
