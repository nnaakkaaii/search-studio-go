import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

// @Controller()の引数にルーティングのパスを指定する
// @Controller()は '/'へのパス
@Controller()
export class AppController {
  // app.service.tsで宣言したクラスをDI
  constructor(private readonly appService: AppService) {}

  // getメソッドを受け取る
  @Get()  // この引数でパスを指定すると、Controllerに追加してパスの指定が可能.
  getHello(): string {
    return this.appService.getHello();
  }
}
